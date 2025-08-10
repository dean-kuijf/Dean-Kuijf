library(shiny)
library(faraway)

# base de dados escolhida
data(fat)

# conversão imperial - metrico
convert_units <- function(weight_kg, height_cm) {
  weight_lbs <- weight_kg / 0.453592
  height_inches <- height_cm / 2.54
  return(list(weight_lbs = weight_lbs, height_inches = height_inches))
}

# calculo do potencial de massa muscular a desenvolver
calcular_massa_muscular <- function(weight, height, wrist, ankle) {
  height_m <- height * 0.0254
  
  massa_muscular <- 22 * (height_m^2) + 
    0.5 * wrist + 
    0.5 * ankle - 10
  
  weight_kg <- weight / 2.20462
  
  massa_muscular_adicional_kg <- max(0, massa_muscular - weight_kg)
  
  return(massa_muscular_adicional_kg)
}

# calculo do imc e categorização em zonas
calculate_imc <- function(weight_lbs, height_inches) {
  weight_kg <- weight_lbs * 0.453592
  height_m <- height_inches * 0.0254
  
  imc <- weight_kg / (height_m^2)
  imc[imc > 100] <- NA
  
  imc_zone <- cut(imc, breaks = c(-Inf, 18.5, 25, Inf), labels = c("Magro", "Normal", "Obeso"))
  
  return(list(imc = imc, zone = imc_zone))
}

#calculo da percentagem de cada zona
calculate_percentages <- function(imc_data) {
  totals <- table(imc_data$zone)
  percentages <- round(100 * totals / sum(totals), 1)
  return(percentages)
}

# calculo do metabolismo basal com a fórmula de Harris-Benedict
BMR_formula <- function(weight, height, age, gender) {
  if (gender == "Male") {
    bmr <- 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
  } else {
    bmr <- 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
  }
  return(bmr)
}

# menu
ui <- fluidPage(
  
  titlePanel("Análise de Dados Corporais"),
  
  sidebarLayout(
    
    sidebarPanel(
      tabsetPanel(
        tabPanel("Análise de Dados",
                 selectInput("variable", "Escolha a variável para observar:", choices = colnames(fat)),
                 actionButton("show_data", "Mostrar Dados"),
                 br(),
                 selectInput("outlier_variable", "Escolha a variável para verificar outliers:", choices = colnames(fat)), 
                 actionButton("show_outliers", "Mostrar Outliers"),
                 br(),
                 numericInput("weight", "Peso próprio (em lbs)", value = 150),
                 numericInput("height", "Altura própria (em polegadas)", value = 65),
                 actionButton("compare", "Comparação com o IMC"),
                 selectInput("gender", "Sexo:", choices = c("Male", "Female")),
                 numericInput("percentual_gordura", "Percentagem de gordura:", value = 15),
                 numericInput("fat_wrist", "Diametro do pulso (polegadas):", value = 17),
                 numericInput("fat_ankle", "Diametro do tornozelo (polegadas):", value = 22),
                 actionButton("calculate_muscle", "Potencial de massa muscular"),
                 numericInput("age","Idade", value = 20),
                 selectInput("goal", "Objetivo a alcançar:", choices = c("Perder peso", "Manter peso", "Ganhar peso")),
                 actionButton("calculate_calories", "Calorias para atingir o objetivo")
        ),
        tabPanel("Conversor de Unidades",
                 numericInput("input_weight", "Peso (kg)", value = 70),
                 numericInput("input_height", "Altura (cm)", value = 170),
                 actionButton("convert_units", "Converter"),
                 textOutput("converted_weight"),
                 textOutput("converted_height")
        )
      )
    ),
    
    mainPanel(
      plotOutput("histogram"),
      verbatimTextOutput("patient_info"),  
      plotOutput("boxplot"),
      textOutput("outlier_info"),
      plotOutput("imc_plot"),
      textOutput("percentages"),
      textOutput("calories_estimate"),
      textOutput("muscle_estimate")
    )
    
  )
  
)

# Definir o servidor
server <- function(input, output) {
  
  output$outlier_info <- renderText({
    if (input$show_outliers > 0) {
      outlier_variable <- input$outlier_variable
      outliers <- boxplot.stats(fat[, outlier_variable])$out
      outlier_row <- fat[which(fat[, outlier_variable] %in% outliers), ]
      
      paste("Informações do Outlier:",
            paste(names(outlier_row), outlier_row, sep = ": ", collapse = ", "),
            collapse = "\n"
      )
    } else {
      NULL
    }
  })
  
  observeEvent(input$show_data, {
    output$histogram <- renderPlot({
      hist(fat[, input$variable], main = input$variable, xlab = "", ylab = "Frequência")
    })
    
    output$patient_info <- renderPrint({
      patient <- fat[which.max(fat[, input$variable]), ]
      cat("Paciente com o maior valor de", input$variable, ":\n")
      print(patient)
      
      patient <- fat[which.min(fat[, input$variable]), ]
      cat("\nPaciente com o menor valor de", input$variable, ":\n")
      print(patient)
    })
  })
  
  observeEvent(input$show_outliers, {
    output$boxplot <- renderPlot({
      boxplot(fat[, input$outlier_variable], col = "red", main = input$outlier_variable, xlab = "Index", ylab = input$outlier_variable)
      
      outliers <- boxplot.stats(fat[, input$outlier_variable])$out
      text(1, outliers, labels = row.names(fat)[which(fat[, input$outlier_variable] %in% outliers)], pos = 4, offset = 0.5, col = "blue")
    })
  })
  
  observeEvent(input$compare, {
    user_imc <- calculate_imc(input$weight, input$height)$imc
    
    output$user_result <- renderText({
      imc_data <- calculate_imc(fat$weight, fat$height)
      user_zone <- cut(user_imc, breaks = c(-Inf, 18.5, 25, Inf), labels = c("Magro", "Normal", "Obeso"))
      
      paste("O seu IMC é", round(user_imc, 2), "e está na zona", user_zone)
    })
    
    output$imc_plot <- renderPlot({
      imc_data <- calculate_imc(fat$weight, fat$height)
      
      plot(imc_data$imc, type = "p", pch = 16, col = imc_data$zone, xlab = "Index", ylab = "IMC", main = "IMC de Todos os Pacientes")
      
      abline(h = c(18.5, 25), lty = 2, col = "gray")
      
      legend("topright", legend = c("Magro", "Normal", "Obeso"), col = c("black", "red", "green"), pch = 16)
      
      points(user_imc, pch = 17, col = "blue", cex = 2)
    })
  })
  
  output$percentages <- renderText({
    if (input$compare > 0) {
      imc_data <- calculate_imc(fat$weight, fat$height)
      percentages <- calculate_percentages(imc_data)
      
      paste0("Percentagem de pacientes:\n", 
             "- Magro: ", percentages['Magro'], "%\n",
             "- Normal: ", percentages['Normal'], "%\n",
             "- Obeso: ", percentages['Obeso'], "%\n",
             "Pacientes na categoria Obeso correm severos riscos à sua saúde, nomeadamente diabetes e doenças cardiovasculares.")
    }
  })
  
  observeEvent(input$calculate_calories, {
    output$calories_estimate <- renderText({
      user_imc <- input$weight / (input$height^2)
      user_goal <- input$goal
      
      if (user_goal == "Perder peso") {
        weight_loss_per_week <- 0.5
        calories_deficit_per_week <- weight_loss_per_week * 7700
        calories_deficit_per_day <- calories_deficit_per_week / 7
        calories_needed_per_day <- BMR_formula(input$weight, input$height, input$age, input$gender) - calories_deficit_per_day
      } else if (user_goal == "Manter peso") {
        calories_needed_per_day <- BMR_formula(input$weight, input$height, input$age, input$gender)
      } else if (user_goal == "Ganhar peso") {
        weight_gain_per_week <- 0.5
        calories_surplus_per_week <- weight_gain_per_week * 7700
        calories_surplus_per_day <- calories_surplus_per_week / 7
        calories_needed_per_day <- BMR_formula(input$weight, input$height, input$age, input$gender) + calories_surplus_per_day
      }
      
      paste("Para", user_goal, "é necessário consumir aproximadamente", round(calories_needed_per_day, 2), "calorias por dia.")
    })
  })
  
  observeEvent(input$calculate_muscle, {
    output$muscle_estimate <- renderText({
      massa_muscular_ganha <- calcular_massa_muscular(input$weight, input$height, input$fat_wrist, input$fat_ankle)
      paste("Tem o potencial de obter", round(massa_muscular_ganha, 2), "kg de massa muscular naturalmente.")
    })
  })
  
  observeEvent(input$convert_units, {
    converted_values <- convert_units(input$input_weight, input$input_height)
    
    output$converted_weight <- renderText({
      paste("Peso em lbs:", round(converted_values$weight_lbs, 2))
    })
    
    output$converted_height <- renderText({
      paste("Altura em inches:", round(converted_values$height_inches, 2))
    })
  })


}


# Rodar a aplicação Shiny
shinyApp(ui = ui, server = server)
