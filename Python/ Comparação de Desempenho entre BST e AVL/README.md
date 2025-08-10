[Descrição do Projeto]
Um sistema completo para comparação de desempenho entre Árvores Binárias de Pesquisa (BST) e Árvores AVL, desenvolvido como projeto de grupo. Implementa análises de complexidade temporal para operações fundamentais (inserção, busca e remoção) em diferentes cenários de dados.

[CATEGORIZAÇÃO DE DESEMPENHO]
O sistema utiliza padrões teóricos de complexidade:

BST ideal: O(log n) para todas operações

BST degenerada: O(n) para todas operações

AVL: O(log n) garantido para todas operações

Funcionalidades
[FUNCIONALIDADES]

Implementação Python - Estruturas de Dados
Árvore Binária de Pesquisa (BST)

Inserção, busca e remoção de elementos

Operações sem balanceamento automático

Árvore AVL

Inserção, busca e remoção balanceadas

Rotações automáticas (simples e duplas)

Manutenção do fator de balanceamento

Implementação Python - Análise de Desempenho
Geração de datasets:

Dados ordenados (cenário de pior caso para BST)

Dados aleatórios (cenário médio)

Medição de tempos de execução:

Cronometragem precisa para operações individuais

Análise comparativa entre estruturas

Visualização gráfica:

Plotagem de resultados para diferentes tamanhos de dados

Comparação lado a lado das estruturas

[COMO UTILIZAR]

Pré-requisitos
Python 3.x instalado

Bibliotecas necessárias:

bash
pip install matplotlib
Executar o Sistema
bash
python projeto_de_grupo(P5).py
[ESTRUTURA DE FICHEIROS]

text
projecto/
│
├── projeto_de_grupo(P5).py    # Implementação completa das árvores e análise
└── README.md                   # Este ficheiro
[FUNCIONALIDADES TÉCNICAS]

Implementação das Estruturas
BST

Nós com ponteiros left/right

Inserção recursiva

Busca por valor

Remoção com três casos (0, 1 ou 2 filhos)

AVL

Nós estendidos com altura

Cálculo do fator de balanceamento

Quatro tipos de rotações

Balanceamento automático após operações

Análise de Desempenho
Testes para tamanhos: 100, 1000 e 10000 elementos

Medição de:

Tempo de inserção em massa

Tempo de busca sequencial

Tempo de remoção em massa

Visualização com Matplotlib

[EXEMPLO DE UTILIZAÇÃO]

Análise Comparativa
python
# Geração de dados aleatórios
data = generate_random_data(1000)

# Criação das árvores
bst = BST()
avl = AVL()

# Medição de desempenho
time_bst = measure_insertion(bst, data)
time_avl = measure_insertion(avl, data)

print(f"BST: {time_bst:.5f}s | AVL: {time_avl:.5f}s")
Visualização de Resultados
python
# Plotagem automática ao executar o script
# Mostra três gráficos comparativos:
# 1. Tempos de inserção
# 2. Tempos de busca
# 3. Tempos de remoção
[TEORIA APLICADA]

Complexidade Assintótica
Operação	BST (melhor)	BST (pior)	AVL (sempre)
Inserção	O(log n)	O(n)	O(log n)
Busca	O(log n)	O(n)	O(log n)
Remoção	O(log n)	O(n)	O(log n)
Fatores de Balanceamento AVL
Calculado como: altura(subárvore esquerda) - altura(subárvore direita)

Árvore balanceada quando |fator| ≤ 1

Requer rotações quando |fator| > 1

[CONTRIBUIÇÃO]
Este é um projecto de grupo desenvolvido para fins educacionais. Para contribuir:

Faça um fork do projecto

Crie um ramo para a sua funcionalidade

Faça commit das suas alterações

Faça um pull request

[LICENÇA]
Este projecto foi desenvolvido como trabalho académico e está disponível para uso educacional.

Desenvolvido por: [Nome da Equipa]
Disciplina: [Nome da Disciplina]
