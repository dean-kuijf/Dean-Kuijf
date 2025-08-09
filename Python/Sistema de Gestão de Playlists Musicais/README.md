# Sistema de Gestão de Playlists Musicais

Um sistema completo em Python para gerir músicas e criar playlists personalizadas, desenvolvido como projecto de grupo.

## [FUNCIONALIDADES]

### Gestão de Músicas
- **Visualizar** todas as músicas registadas
- **Filtrar** músicas por género musical
- **Adicionar** novas músicas ao catálogo
- **Remover** músicas existentes
- **Avaliar** músicas (escala de 1 a 5)
- **Gerar playlist automática** de 60 minutos

### Gestão de Playlists
- **Criar playlists** personalizadas com filtros por:
  - Género musical
  - Artista específico
- **Visualizar** todas as playlists criadas
- **Avaliar** playlists existentes
- **Guardar** playlists automaticamente

## [COMO UTILIZAR]

### Pré-requisitos
- Python 3.x instalado
- Ficheiro `musicas.csv` com as seguintes colunas:
  ```
  Genero,Subgenero,Artista,Titulo,Data de lançamento,tempo,Avaliacao
  ```

### Executar o Sistema
```bash
python Projeto_de_grupo.py
```

### Navegação
O sistema possui dois menus principais:

#### 1. Gerir Músicas
- Opção 1: Mostrar todas as músicas
- Opção 2: Filtrar por género
- Opção 3: Adicionar nova música
- Opção 4: Remover música
- Opção 5: Avaliar músicas
- Opção 6: Gerar playlist de 60 minutos
- Opção 7: Voltar ao menu principal

#### 2. Gerir Playlists
- Opção 1: Ver todas as playlists
- Opção 2: Criar nova playlist
- Opção 3: Avaliar playlist
- Opção 4: Voltar ao menu principal

## [ESTRUTURA DE FICHEIROS]

```
projecto/
│
├── Projeto_de_grupo.py    # Ficheiro principal do sistema
├── musicas.csv           # Base de dados das músicas
├── playlists.csv         # Ficheiro gerado com as playlists
└── README.md            # Este ficheiro
```

## [FORMATO DOS DADOS]

### musicas.csv
```csv
Genero,Subgenero,Artista,Titulo,Data de lançamento,tempo,Avaliacao
Rock,Classic Rock,Queen,Bohemian Rhapsody,1975,5:55,5
Pop,Pop Rock,Michael Jackson,Beat It,1983,4:18,4
```

### Campos obrigatórios:
- **Género**: Categoria principal da música
- **Subgénero**: Subcategoria específica
- **Artista**: Nome do artista/banda
- **Título**: Nome da música
- **Data de lançamento**: Ano de lançamento
- **Tempo**: Duração no formato MM:SS
- **Avaliação**: Nota de 1 a 5

## [FUNCIONALIDADES ESPECIAIS]

### Playlist de 60 Minutos
O sistema gera automaticamente uma playlist equilibrada:
- **10 músicas** com avaliação alta (acima de 4)
- **5 músicas** com avaliação média/baixa (4 ou menos)
- **Duração total**: Máximo de 60 minutos
- **Selecção aleatória** para variedade

### Sistema de Avaliação
- Avalie músicas individuais de 1 a 5
- Avalie playlists completas
- As avaliações são guardadas automaticamente

## [FUNCIONALIDADES TÉCNICAS]

- Leitura e escrita em ficheiros CSV
- Interface de linha de comandos interactiva
- Validação de dados de entrada
- Sistema de filtros múltiplos
- Geração aleatória com restrições de tempo

## [EXEMPLO DE UTILIZAÇÃO]

1. **Iniciar o programa**
   ```bash
   python Projeto_de_grupo.py
   ```

2. **Adicionar uma nova música**
   - Escolha "1" (Gerir músicas)
   - Escolha "3" (Adicionar músicas)
   - Digite as informações solicitadas

3. **Criar uma playlist por género**
   - Escolha "2" (Gerir Playlists)
   - Escolha "2" (Criar playlist)
   - Digite "s" para filtrar por género
   - Digite os géneros desejados

## [CONTRIBUIÇÃO]

Este é um projecto de grupo desenvolvido para fins educacionais. Para contribuir:

1. Faça um fork do projecto
2. Crie um ramo para a sua funcionalidade
3. Faça commit das suas alterações
4. Faça um pull request

## [LICENÇA]

Este projecto foi desenvolvido como trabalho académico e está disponível para uso educacional.

---

**Desenvolvido por:** Dean Kuijf, Francisco Ribeiro 
**Disciplina:** Algoritmia e Programação 
**Ano:** 2023
