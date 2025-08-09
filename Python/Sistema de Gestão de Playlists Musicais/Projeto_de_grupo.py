import csv
import random


def ler_dados_musicas(nome_arquivo):
    musicas = []
    with open(nome_arquivo, 'r') as ficheiro:
        leitor = csv.reader(ficheiro)
        next(leitor)  # Ignora a linha de cabeçalho
        for linha in leitor:
            musica = {
                'Genero': linha[0],
                'Subgenero': linha[1],
                'Artista': linha[2],
                'Titulo': linha[3],
                'Data de lançamento': linha[4],
                'tempo': linha[5],
                'Avaliacao': linha[6]
            }
            musicas.append(musica)
    return musicas


def filtrar_por_genero(musicas, genero):
    return [musica for musica in musicas if musica['Genero'] == genero]


def add_row_to_csv(file_path):
    new_row_data = []
    for i in range(7):
        user_input = input(f"Informação da coluna {i + 1}: ")
        new_row_data.append(user_input)

    with open(file_path, 'a', newline='') as csvfile:
        csvfile.write('\n')
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(new_row_data)

    print("Música adicionada ao arquivo CSV.")


def remove_row_from_csv(file_path, row_index):
    rows = []

    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    if 0 <= row_index < len(rows):
        del rows[row_index]

        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(rows)

        print("Música removida do arquivo CSV.")
    else:
        print("Índice inválido. Por favor, insira um índice válido entre 0 e {len(rows) - 1}.")


def mostrar_musicas(musicas):
    print("Aqui estão todas as músicas:")
    for i, musica in enumerate(musicas, 1):
        print(f"{i}. {musica}")


def menu():
    print("O que deseja fazer à playlist manual?:")
    print("1. Mostrar todas as músicas")
    print("2. Filtrar as musicas por gênero musical")
    print("3. Adicionar músicas")
    print("4. Remover músicas")
    print("5. Avaliar músicas")
    print("6. Gerar playlist de 60 minutos")
    print("7. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha


def avaliar_musica():
    musicas = []
    with open('musicas.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            musicas.append(row)  # Agora pegamos a linha inteira, não apenas o nome da música

    avaliacoes = {}
    for i, musica in enumerate(musicas):
        nome_musica = musica[3]
        avaliacao_inicial = int(musica[6]) if musica[6].isdigit() else None  # Pegamos a avaliação inicial da sétima coluna
        avaliacoes[nome_musica] = avaliacao_inicial

    while True:
        escolha = input("Escolha uma música para avaliar (insira o número correspondente) ou 'sair' para terminar: ")
        if escolha.lower() == 'sair':
            break
        elif escolha.isdigit() and 1 <= int(escolha) <= len(musicas):
            while True:
                avaliacao = input("Avalie a música em uma escala de 1 a 5: ")
                if avaliacao.isdigit() and 1 <= int(avaliacao) <= 5:
                    musica_escolhida = musicas[int(escolha)-1][3]
                    avaliacoes[musica_escolhida] = int(avaliacao)
                    print(f"Você avaliou a música '{musica_escolhida}' com uma nota {avaliacao}.")
                    break
                else:
                    print("Por favor, insira uma avaliação válida.")
        else:
            print("Por favor, escolha uma música válida.")

    print("\nAqui está a sua playlist com as avaliações:")
    for musica, avaliacao in avaliacoes.items():
        print(f"A música '{musica}' tem uma avaliação de {avaliacao}.")

    # Atualiza as avaliações no arquivo CSV
    with open('musicas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for musica in musicas:
            nome_musica = musica[3]
            if nome_musica in avaliacoes:
                musica[6] = avaliacoes[nome_musica]  # Atualiza a avaliação na sétima coluna
            writer.writerow(musica)


def selecionar_musicas(arquivo_csv):
    musicas = []
    with open(arquivo_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            genero = row[0]
            subgenero = row[1]
            artista = row[2]
            titulo = row[3]
            data_lancamento = row[4]
            tempo = sum(int(x) * 60 ** i for i,x in enumerate(reversed(row[5].split(":")))) # Converte o tempo para segundos
            avaliacao = int(row[6])
            musicas.append((genero, subgenero, artista, titulo, data_lancamento, tempo, avaliacao))

    musicas_com_avaliacao_alta = [musica for musica in musicas if musica[6] > 4]
    musicas_com_avaliacao_baixa = [musica for musica in musicas if musica[6] <= 4]

    playlist = []
    total_tempo = 0

    # Adiciona 10 músicas com avaliação alta
    for _ in range(10):
        while True:
            musica = random.choice(musicas_com_avaliacao_alta)
            if total_tempo + musica[5] <= 3600:
                playlist.append(musica)
                total_tempo += musica[5]
                musicas_com_avaliacao_alta.remove(musica)  # Remove a música da lista para evitar duplicatas
                break

    # Adiciona 5 músicas com avaliação baixa
    for _ in range(5):
        while True:
            musica = random.choice(musicas_com_avaliacao_baixa)
            if total_tempo + musica[5] <= 3600:
                playlist.append(musica)
                total_tempo += musica[5]
                musicas_com_avaliacao_baixa.remove(musica)  # Remove a música da lista para evitar duplicatas
                break

    return playlist


def ler_playlists(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        leitor = csv.reader(f)
        playlists = list(leitor)
    return playlists


def mostrar_playlists(playlists):
    for i, playlist in enumerate(playlists):
        if playlist and "Playlist" in playlist[0]:
            avaliacao = playlist[1] if len(playlist) > 1 else "Sem avaliação"  # Adicionado a verificação da avaliação
            print(f"\n{playlist[0]} Avaliação: {avaliacao}")
        elif playlist:
            print(f"Gênero: {playlist[0]}, Subgênero: {playlist[1]}, Artista: {playlist[2]}, Título: {playlist[3]}, Data de lançamento: {playlist[4]}, Tempo: {playlist[5]}, Avaliação: {playlist[6]}")


def read_music_data(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        leitor = csv.reader(f)
        musicas = list(leitor)
    return musicas

def filtrar_por_generos(musicas, generos):
    return [musica for musica in musicas if musica[0] in generos]

def filtrar_por_artista(musicas, artista):
    return [musica for musica in musicas if musica[2] == artista]

def gerar_playlist(musicas, num_musicas):
    if num_musicas > len(musicas):
        print("O número de músicas escolhido é maior do que o número de músicas disponíveis.")
        return None
    else:
        indices_aleatorios = random.sample(range(len(musicas)), num_musicas)
        playlist = [musicas[i] for i in indices_aleatorios]
        return playlist

def salvar_playlist(playlist, nome_arquivo, nome_playlist):
    with open(nome_arquivo, 'a', newline='') as f:
        escritor = csv.writer(f)
        # Adicionar um espaço de duas linhas entre cada playlist
        escritor.writerow([])
        escritor.writerow(["Playlist " + nome_playlist])
        escritor.writerows(playlist)



def avaliar_playlist(playlists, nome_arquivo):
    indices_playlists = [i for i, playlist in enumerate(playlists) if playlist and "Playlist" in playlist[0]]
    for i, indice in enumerate(indices_playlists, 1):
        print(f"{i}. {playlists[indice][0]}")
    while True:
        try:
            indice_playlist = int(input("Por favor, escolha o número da playlist que deseja avaliar: ")) - 1
            if indice_playlist < 0 or indice_playlist >= len(indices_playlists):
                raise ValueError
            avaliacao = input("Por favor, avalie a playlist de 1 a 5: ")
            # Verifica se a avaliação do usuário já existe, se sim, atualiza, se não, adiciona
            if len(playlists[indices_playlists[indice_playlist]]) > 1:
                playlists[indices_playlists[indice_playlist]][1] = f"Avaliacao do Usuario: {avaliacao}"
            else:
                playlists[indices_playlists[indice_playlist]].append(f"Avaliacao do Usuario: {avaliacao}")
            with open(nome_arquivo, 'w', newline='') as f:
                escritor = csv.writer(f)
                escritor.writerows(playlists)
            break
        except ValueError:
            print("Número inválido. Tente novamente.")


def menu_principal():
    print("Menu Principal")
    print("1. Gerenciar músicas")
    print("2. Gerenciar Playlists")
    print("3. SAIR")
    escolha = input("Escolha uma opção: ")
    return escolha


def menu_automatico():
    while True:
        print("\nMenu Automático")
        print("1. Ver todas as playlists")
        print("2. Criar playlist")
        print("3. Avaliar playlist")
        print("4. Sair")

        opcao = input("Por favor, escolha uma opção: ")

        if opcao == '1':
            playlists = ler_playlists('playlists.csv')
            mostrar_playlists(playlists)
        elif opcao == '2':
            musicas = read_music_data('musicas.csv')
            filtrar_genero = input("Deseja filtrar as músicas por gênero? (s/n): ")
            if filtrar_genero.lower() == 's':
                while True:
                    generos_escolhidos = input("Por favor, insira os gêneros musicais que deseja para a playlist (separados por vírgula): ")
                    generos_escolhidos = [genero.strip() for genero in generos_escolhidos.split(",")]
                    musicas_filtradas = filtrar_por_generos(musicas, generos_escolhidos)
                    if musicas_filtradas:
                        break
                    else:
                        print("Gênero inválido. Tente novamente.")
            else:
                filtrar_artista = input("Deseja filtrar as músicas por artista? (s/n): ")
                if filtrar_artista.lower() == 's':
                    while True:
                        artista_escolhido = input("Por favor, insira o nome do artista que deseja para a playlist: ")
                        musicas_filtradas = filtrar_por_artista(musicas, artista_escolhido)
                        if musicas_filtradas:
                            break
                        else:
                            print("Artista inválido. Tente novamente.")
                else:
                    musicas_filtradas = musicas
            num_musicas = int(input("Quantas músicas você quer na playlist? "))
            playlist = gerar_playlist(musicas_filtradas, num_musicas)
            if playlist is not None:
                nome_playlist = input("Por favor, dê um nome para a playlist: ")
                salvar_playlist(playlist, 'playlists.csv', nome_playlist)
                print(f"'Playlist {nome_playlist}' criada e salva em 'playlists.csv'.")

        elif opcao == '3':
            playlists = ler_playlists('playlists.csv')
            avaliar_playlist(playlists, 'playlists.csv')

        elif opcao == '4':
            break


musicas = ler_dados_musicas('musicas.csv')

while True:
    escolha_principal = menu_principal()
    if escolha_principal == '1':
        while True:
            escolha = menu()
            if escolha == '1':
                mostrar_musicas(musicas)
            elif escolha == '2':
             genero_escolhido = input("Por favor, insira o gênero musical que deseja filtrar: ")
             musicas_filtradas = filtrar_por_genero(musicas, genero_escolhido)
             print("Aqui estão as músicas filtradas:")
             for musica in musicas_filtradas:
                    print(musica)
            elif escolha == '3':
                add_row_to_csv('musicas.csv')
            elif escolha == '4':
                row_index_to_remove = int(input("Insira o índice da música a ser removida: "))
                remove_row_from_csv('musicas.csv', row_index_to_remove)
            elif escolha == '5':
                avaliar_musica()
                print("Avaliando músicas...")
            elif escolha == '6':
                print ("PLAYLIST DE 60 MINUTOS:")
                playlist = selecionar_musicas('musicas.csv')
                for i, (genero, subgenero, artista, titulo, data_lancamento, tempo, avaliacao) in enumerate(playlist, 1):
                    minutos, segundos = divmod(tempo, 60)
                    print(f"{i}. Gênero: {genero}, Subgênero: {subgenero}, Artista: {artista}, Título: {titulo}, Data de lançamento: {data_lancamento}, Tempo: {minutos}:{segundos:02d}, Avaliação: {avaliacao}")
            elif escolha == '7':
                print("Voltando ao Menu Principal...")
                break  # Volta ao menu principal
            else:
                print("Opção inválida. Tente novamente.")
    elif escolha_principal == '2':
      menu_automatico()
      
    elif escolha_principal == '3':
        print("A sair do programa")
        break
         # Sai do programa
    else:
        print("Opção inválida. Tente novamente.")

