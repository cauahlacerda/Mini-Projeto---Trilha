import json

with open("C:\\Users\\caual\\OneDrive\\Documentos\\Área de Trabalho\\mini projeto - trilha\\movies_and_series.json") as arquivo:
    data = json.load(arquivo)

arquivo_txt = "C:\\Users\\caual\\OneDrive\\Documentos\\Área de Trabalho\\mini projeto - trilha\\movies_and_series.txt"

with open(arquivo_txt, 'w', encoding='utf-8') as file:
    movie = data['data']['movies'][0]
    serie = data['data']['series'][0]

    # Listar todos os títulos de filmes:
    file.write("Título do Filme:\n")
    file.write(f"- {movie['title']}\n")
    file.write("============================================\n")
    
    # Listar todas as séries:
    file.write("Título da Série:\n")
    file.write(f"- {serie['title']}\n")
    file.write("============================================\n")

    # Recuperar o filme/série com maior nota (rating):
    if movie['rating'] > serie['rating']:
        highest_title = movie['title']
        highest_rating = movie['rating']
    else:
        highest_title = serie['title']
        highest_rating = serie['rating']

    file.write("Recuperar o filme/série com maior nota (rating):\n")
    file.write(f"- {highest_title} ({highest_rating})\n")
    file.write("============================================\n")

    # Listar os gêneros de todos os filmes e séries:
    titulo_filme = movie['title']  
    titulo_serie = serie['title'] 
    generos_filmes = movie['genres']
    generos_series = serie['genres']  

    file.write("Gêneros de todos os filmes e séries:\n")
    file.write(f"\nGêneros de {titulo_filme}:\n")  
    file.write(f"- {', '.join(generos_filmes)}\n")  
    file.write(f"Gêneros de {titulo_serie}:\n")  
    file.write(f"- {', '.join(generos_series)}\n")  

    file.write("============================================\n")

    # Obter o número total de filmes e séries:
    total_movies = len(data['data']['movies'])
    total_series = len(data['data']['series'])
    file.write("Número total de filmes e séries:\n")
    file.write(f"- Total de Filmes: {total_movies}\n")
    file.write(f"- Total de Séries: {total_series}\n")
    file.write("============================================\n")

    # Listar todas as plataformas de streaming disponíveis:
    streaming_platforms = []

    if 'streaming' in movie:
        for platform in movie['streaming']:
            if platform not in streaming_platforms:
                streaming_platforms.append(platform)

    if 'streaming' in serie:
        for platform in serie['streaming']:
            if platform not in streaming_platforms:
                streaming_platforms.append(platform)

    file.write("Plataformas de Streaming Disponíveis:\n")
    file.write(f"- {', '.join(streaming_platforms)}\n")
    file.write("============================================\n")
    
    # Filtrar os filmes/séries disponíveis em 4K no Netflix:
    file.write("Filmes/séries disponíveis em 4K no Netflix:\n")

    if movie['streaming']['Netflix']['available'] and '4K' in movie['streaming']['Netflix']['resolution']:
        file.write(f"- {movie['title']}\n")

    if serie['streaming']['Netflix']['available'] and '4K' in serie['streaming']['Netflix']['resolution']:
        file.write(f"- {serie['title']}\n")

    file.write("============================================\n")
    
    # Identificar plataformas onde um filme específico está disponível:
    titulo_filme = movie['title']
    file.write("Identificar plataformas onde um filme específico está disponível:\n")
    file.write(f"Filme: {titulo_filme}\n")

    streaming = movie.get('streaming', {})
    platform = list(streaming.keys())[0] 
    details = streaming[platform] 

    if details and details['available']:
        file.write(f"- {platform}: {details['url']}\n")
    file.write("============================================\n")

    # Listar todos os atores e os personagens que interpretam:
    file.write("Todos os atores e os personagens que interpretam:\n")
    for cast in movie['cast']:
        file.write(f"- {cast['actor']} como {cast['character']}\n")
    for cast in serie['cast']:
        file.write(f"- {cast['actor']} como {cast['character']}\n")
    file.write("============================================\n")

    # Obter o ator com maior salário em um filme ou série:
    ator_maior_salario = None
    maior_salario = 0
    for movie in data["data"]["movies"]:
        for actor in movie["cast"]:
            if actor["salary"] > maior_salario:
                maior_salario = actor["salary"]
                ator_maior_salario = actor

    file.write(f"Ator com maior salário: {ator_maior_salario['actor']} (Salário: {ator_maior_salario['salary']:,.2f})\n")
    file.write("============================================\n")
        
    # Listar todas as localizações de filmagem dos filmes:
    titulo_filme = movie['title']  
    file.write("Todas as localizações de filmagem dos filmes:\n")
    file.write(f"Filme: {titulo_filme}\n")  
    filming_locations = set(movie['production']['filmingLocations'])
    file.write(f"- {', '.join(filming_locations)}\n")
    file.write("============================================\n")

    # Listar os diretores de cada filme:
    file.write("Diretor do filme:\n")
    file.write(f"- {movie['title']}: {', '.join(movie['directors'])}\n")
    file.write("============================================\n")

    # Obter o filme com maior receita na bilheteria (revenue):
    file.write("Filme com maior receita na bilheteira (revenue):\n")
    file.write(f"- {movie['title']} (${movie['production']['boxOffice']['revenue']:,})\n")
    file.write("============================================\n")

    # Calcular o lucro médio dos filmes:
    average_profit = movie['production']['boxOffice']['profit']
    file.write("Lucro médio dos filmes:\n")
    file.write(f"- Média do Lucro: ${average_profit:,.2f}\n")
    file.write("============================================\n")

    # Obter a distribuição de vendas de ingressos por região:
    file.write("Distribuição de vendas de ingressos por região:\n")
    ticket_sales = movie['production']['boxOffice']['ticketSales']
    file.write(f"- {movie['title']}: Nacional: ${ticket_sales['domestic']:,}, Internacional: ${ticket_sales['international']:,}\n")
    file.write("============================================\n")

    # Listar todos os prêmios e categorias de cada filme/série:
    file.write("Todos os prêmios e categorias de cada filme/série:\n")
    for award in movie['awards']:
        file.write(f"- {award['award']}: {award['year']}, {award['category']} (Filme: {movie['title']})\n")

    for award in serie['awards']:
        file.write(f"- {award['award']}: {award['year']}, {award['category']} (Série: {serie['title']})\n")
    file.write("============================================\n")

    # Identificar filmes/séries que ganharam prêmios:
    file.write("Filmes/séries que ganharam prêmios:\n")

    premio_ganho_filme = False
    for award in movie['awards']:
        if award['won']:
            file.write(f"- {movie['title']}\n")
            premio_ganho_filme = True
            break  

    premio_ganho_serie = False
    for award in serie['awards']:
        if award['won']:
            file.write(f"- {serie['title']}\n")
            premio_ganho_serie = True
            break 

    file.write("============================================\n")

    # Listar os indicados ao prêmio de 'Melhor Filme' de cada ano:
    file.write("Os indicados ao prêmio de 'Melhor Filme' de cada ano:\n")
    for award in movie['awards']:
        if award['category'] == "Best Picture":
            file.write(f"- {award['year']}: {', '.join(award['nominees'])}\n")
    file.write("============================================\n")

    # Obter o comentário com maior número de votos úteis (helpfulVotes):
    file.write("Comentário com mais votos úteis:\n")
    comentarios = []

    for review in movie['reviews']:
        votos_util = review['details']['helpfulVotes']
        comentario = review['comment']
        comentarios.append((votos_util, comentario))

    maior_voto = max(comentarios)  
    file.write(f"- {maior_voto[1]} ({maior_voto[0]} votos úteis)\n")
    file.write("============================================\n")

    # Calcular a nota média dos filmes:
    average_rating = movie['rating']  
    file.write("A nota média dos filmes:\n")
    file.write(f"- Média das Notas: {average_rating:.1f}\n")
    file.write("============================================\n")

    # Filtrar todas as avaliações feitas antes de 2022:
    file.write("Todas as avaliações feitas antes de 2022:\n")
    for review in movie['reviews']:
        if review['details']['date'] < '2022-01-01':
            file.write(f"- {review['comment']} (Data: {review['details']['date']})\n")
    file.write("============================================\n")
