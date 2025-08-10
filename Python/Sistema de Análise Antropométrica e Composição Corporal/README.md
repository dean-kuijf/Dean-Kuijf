## [CATEGORIZAÇÃO DO IMC]

O sistema utiliza as categorias padrão da OMS:
- **Magro**: IMC < 18.5
- **Normal**: 18.5 ≤ IMC < 25
- **Obeso**: IMC ≥ 25

### Alertas de Saúde (Aplicação Shiny)
A aplicação R inclui alertas automáticos sobre riscos associados à obesidade:
- **Diabetes tipo 2**
- **Doenças cardiovasculares**
- **Outros riscos metabólicos**# Sistema de Análise Antropométrica e Composição Corporal

Um sistema completo com implementações em **Python** e **R (Shiny)** para análise de dados antropométricos, cálculo de IMC, estimativa de potencial de massa muscular e planeamento nutricional, desenvolvido como projecto de grupo.

## [FUNCIONALIDADES]

### Implementação Python - Análise de Dados
- **Visualizar** estatísticas descritivas e distribuições das variáveis antropométricas
- **Análise de correlações** entre variáveis específicas ou todas as variáveis
- **Identificar** valores ausentes no dataset
- **Detectar** valores discrepantes (outliers) com método IQR

### Implementação Python - Comparação com Utilizador
- **Calcular IMC** do utilizador e comparar com pacientes do dataset
- **Visualização gráfica** do IMC com categorização por cores
- **Categorização automática** (Magro, Normal, Obeso)
- **Posicionamento** do utilizador no contexto dos dados

### Implementação Python - Calculadora de Massa Muscular
- **Estimar** potencial de ganho de massa muscular natural
- **Validação** de dados de entrada com limites realistas
- **Cálculo baseado** em altura, peso, contorno do pulso e tornozelo

### Implementação R (Shiny) - Interface Web Interactiva
- **Dashboard web** com interface gráfica intuitiva
- **Análise visual** de variáveis com histogramas e boxplots
- **Detecção de outliers** com informações detalhadas dos pacientes
- **Comparação de IMC** com visualização em tempo real
- **Calculadora de calorias** baseada na fórmula Harris-Benedict
- **Conversor de unidades** (métrico ↔ imperial)
- **Planeamento nutricional** por objectivos (perder/manter/ganhar peso)

## [COMO UTILIZAR]

### Implementação Python

#### Pré-requisitos
- Python 3.x instalado
- Bibliotecas necessárias:
  ```bash
  pip install pandas matplotlib seaborn
  ```
- Ficheiro `DATASET_FAT.csv` com dados antropométricos

#### Executar o Sistema Python
```bash
python trabalho_de_grupo_1.py
```

### Implementação R (Shiny)

#### Pré-requisitos
- R instalado
- Pacotes necessários:
  ```r
  install.packages(c("shiny", "faraway"))
  ```

#### Executar a Aplicação Shiny
```r
# Executar directamente no RStudio ou terminal R
source("trabalho_de_grupoR_1.R")
```
A aplicação abrirá automaticamente no browser predefinido.

### Navegação

#### Sistema Python - Menu Principal
O sistema possui um menu principal com três opções:

**1. Explorar o Dataset**
- **Opção 1**: Estatísticas descritivas e distribuição das variáveis
- **Opção 2**: Correlações entre variáveis (específicas ou todas)
- **Opção 3**: Identificar valores ausentes
- **Opção 4**: Detectar valores discrepantes (outliers)

**2. Comparar Dados com o Utilizador**
- **Opção 1**: Calcular e comparar IMC com pacientes
- Introduzir peso (kg) e altura (metros)
- Visualizar posição no gráfico comparativo

**3. Calcular Massa Muscular Futura**
- Introduzir dados antropométricos:
  - Altura: 150-210 cm
  - Peso: 50-150 kg
  - Contorno do tornozelo: 18-35 cm
  - Contorno do pulso: 14-22 cm

#### Aplicação R (Shiny) - Interface Web
A aplicação possui dois separadores principais:

**Separador "Análise de Dados":**
- **Análise de variáveis**: Seleccionar variável e visualizar histograma
- **Detecção de outliers**: Boxplots com identificação de valores extremos
- **Comparação de IMC**: Introduzir peso e altura para comparar com dataset
- **Calculadora de massa muscular**: Estimar potencial de ganho muscular
- **Planeamento nutricional**: Calcular calorias necessárias por objectivo
- **Selecção de género e idade**: Para cálculos personalizados

**Separador "Conversor de Unidades":**
- **Conversão métrico ↔ imperial**: kg/cm para lbs/inches
- **Conversão automática**: Resultados instantâneos

## [ESTRUTURA DE FICHEIROS]

```
projecto/
│
├── trabalho_de_grupo_1.py       # Sistema Python (linha de comandos)
├── trabalho_de_grupoR_1.R       # Aplicação Shiny R (interface web)
├── DATASET_FAT.csv              # Dataset com dados antropométricos
└── README.md                    # Este ficheiro
```

## [FORMATO DOS DADOS]

### DATASET_FAT.csv
O ficheiro deve conter as seguintes colunas (compatível com o dataset `faraway::fat` do R):
```csv
brozek,siri,density,age,weight,height,adiposity,free,neck,chest,abdomen,hip,thigh,knee,ankle,biceps,forearm,wrist
12.3,12.6,1.0708,23,154.25,67.75,23.7,134.9,36.2,93.1,85.2,94.5,59.0,37.3,21.9,32.0,27.4,17.1
```

### Campos principais:
- **age**: Idade dos pacientes
- **weight**: Peso em libras
- **height**: Altura em polegadas  
- **wrist**: Contorno do pulso em centímetros
- **ankle**: Contorno do tornozelo em centímetros
- **Outras variáveis**: Medidas antropométricas detalhadas (densidade, percentagem de gordura, etc.)

## [FUNCIONALIDADES ESPECIAIS]

### Sistema Python - Análise Estatística Avançada
- **Histogramas com KDE** para visualização de distribuições
- **Matriz de correlação** com mapa de calor interactivo
- **Detecção de outliers** usando método IQR (Intervalo Interquartil)
- **Estatísticas descritivas** completas para cada variável

### Aplicação Shiny R - Interface Interactiva
- **Dashboard responsivo** com actualizações em tempo real
- **Visualizações dinâmicas** que se adaptam aos dados introduzidos
- **Identificação de outliers** com informações completas do paciente
- **Cálculo automático de percentagens** por categoria de IMC
- **Alertas de saúde** baseados na categorização de obesidade

### Validação de Dados Comum
- **Limites realistas** para todas as medidas antropométricas
- **Tratamento de erros** com mensagens informativas
- **Verificação automática** de intervalos válidos
- **Conversão automática** entre sistemas métrico e imperial

### Visualizações Gráficas Avançadas
- **Gráficos de dispersão** coloridos por categoria (Python)
- **Histogramas interactivos** com informações detalhadas (Shiny)
- **Boxplots** com identificação visual de outliers (Shiny)
- **Mapas de calor** para correlações (Python)
- **Marcação especial** do utilizador nos gráficos (ambos)

## [FUNCIONALIDADES TÉCNICAS]

### Implementação Python
- Processamento de dados com Pandas
- Visualizações com Matplotlib e Seaborn
- Interface de linha de comandos interactiva
- Cálculos antropométricos baseados em fórmulas científicas
- Sistema de categorização automática de IMC
- Validação robusta de dados de entrada

### Implementação R (Shiny)
- Framework Shiny para aplicações web interactivas
- Dataset `faraway::fat` integrado
- Interface reactiva com actualizações automáticas
- Conversão automática de unidades (métrico ↔ imperial)
- Cálculo de TMB com fórmula Harris-Benedict
- Planeamento nutricional personalizado
- Validação de entrada com feedback visual

## [EXEMPLO DE UTILIZAÇÃO]

### Sistema Python

1. **Explorar correlações no dataset**
   ```bash
   python trabalho_de_grupo_1.py
   # Escolher opção 1 (Explorar dataset)
   # Escolher opção 2 (Correlações)
   # Seleccionar variáveis específicas
   ```

2. **Calcular o seu IMC**
   ```bash
   # Escolher opção 2 (Comparar dados)
   # Escolher opção 1 (IMC)
   # Introduzir peso: 70 kg
   # Introduzir altura: 1.75 m
   ```

3. **Estimar potencial de massa muscular**
   ```bash
   # Escolher opção 3 (Massa muscular)
   # Introduzir medidas antropométricas
   # Receber estimativa personalizada
   ```

### Aplicação Shiny R

1. **Análise de variável específica**
   ```r
   # Seleccionar variável no menu dropdown
   # Clicar "Mostrar Dados"
   # Visualizar histograma e informações dos pacientes
   ```

2. **Calcular necessidades calóricas**
   ```r
   # Introduzir peso, altura, idade
   # Seleccionar género e objectivo
   # Clicar "Calorias para atingir o objetivo"
   # Receber plano nutricional personalizado
   ```

3. **Converter unidades**
   ```r
   # Ir ao separador "Conversor de Unidades"
   # Introduzir peso em kg e altura em cm
   # Clicar "Converter"
   # Obter valores em libras e polegadas
   ```

## [FÓRMULAS UTILIZADAS]

### Cálculo de IMC
```
IMC = Peso (kg) / Altura (m)²
```

### Estimativa de Massa Muscular
```
Massa Muscular = 22 × (altura_m)² + 0.5 × pulso + 0.5 × tornozelo - 10
Potencial de Ganho = max(0, Massa Muscular - Peso Actual)
```

### Taxa Metabólica Basal (Harris-Benedict)
**Homens:**
```
TMB = 88.362 + (13.397 × peso_kg) + (4.799 × altura_cm) - (5.677 × idade)
```

**Mulheres:**
```
TMB = 447.593 + (9.247 × peso_kg) + (3.098 × altura_cm) - (4.330 × idade)
```

### Planeamento Calórico
- **Perder peso**: TMB - 550 cal/dia (0.5 kg/semana)
- **Manter peso**: TMB
- **Ganhar peso**: TMB + 550 cal/dia (0.5 kg/semana)

### Conversão de Unidades
- **kg para lbs**: kg ÷ 0.453592
- **cm para inches**: cm ÷ 2.54

## [CONTRIBUIÇÃO]

Este é um projecto de grupo desenvolvido para fins educacionais. Para contribuir:

1. Faça um fork do projecto
2. Crie um ramo para a sua funcionalidade
3. Faça commit das suas alterações
4. Faça um pull request

## [LICENÇA]

Este projecto foi desenvolvido como trabalho académico e está disponível para uso educacional.

---

**Desenvolvido por:** Dean Kuijf, Francisco Ribeiro, Diogo Silva, Duarte Melo
**Disciplina:** Laboratórios de estatistica  
**Ano:** 2024
