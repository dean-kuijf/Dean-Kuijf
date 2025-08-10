import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# import mplcursors
def carregar_dataset(nome_arquivo):
    return pd.read_csv(nome_arquivo)


def visualizar_estatisticas_e_distribuicao(data):
    print("Estatísticas descritivas e distribuição das variáveis:")
    for column in data.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f"Distribuição de {column}")
        plt.xlabel(column)
        plt.ylabel("Frequência")
        plt.show()
        print("\nEstatísticas descritivas de", column)
        print(data[column].describe())


def identificar_correlacoes(data):
    while True:
        print("\nEscolha uma opção:")
        print("1. Correlação entre variáveis específicas")
        print("2. Correlação entre todas as variáveis")
        opcao = input("Opção: ")

        if opcao == "1":
            print("Escolha as variáveis para identificar correlações (separadas por espaços):")
            print("Variáveis disponíveis:")
            for i, var in enumerate(data.columns, 1):
                print(f"{i}. {var}")

            opcoes = input("Digite os números correspondentes às variáveis (separados por espaço): ")
            opcoes = opcoes.split()

            if len(set(opcoes)) == len(opcoes) and all(
                    opcao.isdigit() and 1 <= int(opcao) <= len(data.columns) for opcao in opcoes):
                variaveis = [data.columns[int(opcao) - 1] for opcao in opcoes]
                correlation_matrix = data[variaveis].corr().round(1)  # Arredondamento para uma casa decimal
                correlation_matrix = (correlation_matrix + 1) * 50  # Scaling to 0-100
                correlation_matrix[correlation_matrix < 0] = 0
                print("\nMatriz de correlação entre as variáveis selecionadas:")
                print(correlation_matrix)
                plt.figure(figsize=(10, 8))
                sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".1f", linewidths=0.5, vmin=0,
                            vmax=100)
                plt.title("Matriz de Correlação")
                plt.show()
                break
            else:
                print("Opção inválida. Por favor, escolha opções válidas e não repita variáveis.")
        elif opcao == "2":
            print("Matriz de correlação entre todas as variáveis:")
            correlation_matrix = data.corr().round(1)  # Arredondamento para uma casa decimal
            correlation_matrix = (correlation_matrix + 1) * 50  # Scaling to 0-100
            correlation_matrix[correlation_matrix < 0] = 0
            print(correlation_matrix)
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".1f", linewidths=0.5, vmin=0, vmax=100)
            plt.title("Matriz de Correlação")
            plt.show()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def identificar_valores_ausentes(data):
    print("Valores ausentes:")
    print(data.isnull().sum())


def identificar_valores_discrepantes(data):
    print("Valores discrepantes (outliers):")
    for column in data.columns:
        q1 = data[column].quantile(0.25)
        q3 = data[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)][column]
        print(f"{column}:")
        for index, value in outliers.items():
            print(f"Index: {index}, Value: {value}")
            print("-" * 50)  # Linha de separação entre cada par de índice e valor de outlier


def massa_corporal(altura, pulso, tornozelo, peso):
    massa_muscular = 22 * ((altura * 0.01) ** 2) + 0.5 * pulso + 0.5 * tornozelo - 10
    # massa_muscular_adicional_kg = peso - massa_muscular_inicial
    massa_muscular_adicional_kg = max(0, massa_muscular - peso)
    result = round(massa_muscular_adicional_kg, 2)

    return result


def menu_massa_corporal():
    while True:
        altura = input('Digite a sua altura (cm) (min. 150 e max 210): ')
        if 150 <= int(altura) <= 210:
            break
        else:
            print('Valor irrealista. Por favor, seja prudente.')

    while True:
        peso = input('Digite o seu peso (kg) (min. 50 e max. 150): ')
        if 50 <= float(peso) <= 150:
            break
        else:
            print('Valor irrealista. Por favor, seja prudente.')

    while True:
        tornozelo = input('Insira o comprimento do contorno do seu tornozelo (cm) (min. 18 e max. 35): ')
        if 18 <= float(tornozelo) <= 35:
            break
        else:
            print('Valor irrealista. Por favor, seja prudente.')

    while True:
        pulso = input('Insira o comprimento do contorno do seu pulso (cm) (min. 14 e max. 22): ')
        if 14 <= float(pulso) <= 23:
            break
        else:
            print('Valor irrealista. Por favor, seja prudente.')

    # Call the massa_corporal function with user's inputs and store the result
    result_final = massa_corporal(int(altura), float(pulso), float(tornozelo), float(peso))

    # Print the result
    print("O potencial de massa muscular em kg que podera ganhar naturalmente é:", result_final)

    # Call the menu function
    menu_principal()


def explorar_dataset(data):
    while True:
        print("\nEscolha uma opção para explorar o dataset:")
        print("1. Visualizar estatísticas descritivas e distribuição das variáveis antropometricas")
        print("2. Visualizar correlações entre as variáveis antropometricas")
        print("3. Visualizar valores ausentes")
        print("4. Identificar valores descrepantes (outliers)")
        print("0. Voltar ao Menu Principal")
        opcao = input("Opção: ")

        if opcao == "1":
            visualizar_estatisticas_e_distribuicao(data)
        elif opcao == "2":
            identificar_correlacoes(data)
        elif opcao == "3":
            identificar_valores_ausentes(data)
        elif opcao == "4":
            identificar_valores_discrepantes(data)
        elif opcao == "0":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC)"""
    return peso / (altura ** 2)


# PS: HAVIA UM OUTLIER GIGANTE NO IMC (PESO 120KG , ALTURA 74CM)

def categorizar_imc(imc):
    """Categoriza o IMC em 'Magro', 'Normal' ou 'Obeso'."""
    if imc < 18.5:
        return 'Magro'
    elif imc < 25:
        return 'Normal'
    else:
        return 'Obeso'


def plotar_grafico_imc(data, imc_usuario):
    """Plota um gráfico de pontos com o IMC dos pacientes, incluindo o usuário."""
    # Categorizar o IMC dos pacientes
    data['Categoria_IMC'] = data['IMC'].apply(categorizar_imc)

    # Definir cores com base na categoria de IMC
    cores = {'Magro': 'blue', 'Normal': 'green', 'Obeso': 'red'}

    # Plotar o gráfico de pontos do IMC
    plt.figure(figsize=(10, 6))
    for categoria, cor in cores.items():
        categoria_data = data[data['Categoria_IMC'] == categoria]
        plt.scatter(categoria_data.index, categoria_data['IMC'], color=cor, label=categoria)
    plt.scatter(len(data), imc_usuario, color='orange', label='Você', marker='x', s=100)
    plt.title('IMC dos Pacientes')
    plt.xlabel('Paciente')
    plt.ylabel('IMC')
    plt.legend()
    plt.grid(True)
    plt.show()


def IMC():
    # Carregar o conjunto de dados
    data = pd.read_csv("DATASET_FAT.csv")

    # Solicitar ao usuário o peso (em kg) e altura (em metros)
    while True:
        try:
            peso = float(input("Digite o seu peso (kg): "))
            if peso <= 0 or peso > 1000:  # Intervalo realista para peso
                raise ValueError("O peso deve estar entre 0 e 1000 kg.")
            altura = float(input("Digite a sua altura (metros): "))
            if altura <= 0 or altura > 3:  # Intervalo realista para altura (3 metros é improvável)
                raise ValueError("A altura deve estar entre 0 e 3 metros.")
            break
        except ValueError as ve:
            print(ve)

    # Calcular o IMC do usuário
    imc_usuario = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc_usuario:.2f}")

    # Adicionar a coluna de IMC ao DataFrame
    data['IMC'] = data.apply(lambda row: calcular_imc(row['Peso (kg)'], row['Altura (cm)'] / 100), axis=1)

    # Plotar o gráfico de pontos do IMC
    plotar_grafico_imc(data, imc_usuario)

    # Categorizar o IMC do usuário
    categoria_usuario = categorizar_imc(imc_usuario)
    print(f"Com base no seu IMC, você está categorizado como: {categoria_usuario}")


def menu_comparacao_utilizador(data):
    while True:
        print("")
        print("IMC DO UTILIZADOR E PACIENTES")
        print("1.IMC do utilizador e pacientes")
        print("2. Outra opção")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            IMC()
        elif escolha == '2':
            print("Implemente sua outra opção aqui.")
        elif escolha == '3':
            print("A voltar ao menu pricipal...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def menu_principal():
    nome_arquivo = "DATASET_FAT.csv"
    data = carregar_dataset(nome_arquivo)
    while True:
        print("\nMenu Principal:")
        print("1. Explorar o dataset")
        print("2. Comparar dados com o utilizador")
        print("3. Calcular massa muscular futura")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            explorar_dataset(data)
        elif opcao == "2":
            data = pd.read_csv("DATASET_FAT.csv")
            menu_comparacao_utilizador(data)
        elif opcao == "3":
            menu_massa_corporal()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


menu_principal()
