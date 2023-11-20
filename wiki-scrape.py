import requests
from bs4 import BeautifulSoup

# Define a URL da página web que será scrapeda
url = "https://www.naeu.playblackdesert.com/en-US/Wiki"

# Faz uma requisição HTTP para a URL e obtém o conteúdo HTML da página
response = requests.get(url)
html_content = response.content

# Cria um objeto BeautifulSoup para analisar o HTML da página
soup = BeautifulSoup(html_content, "html.parser")

# Encontra todos os tópicos na página
topics = soup.find_all("li", class_="list_wrap show active")

# Abre um arquivo de texto chamado "output.txt" para escrita
with open("output.txt", mode="w", encoding="utf-8") as txt_file:

    # Itera sobre cada tópico encontrado na página
    for topic in topics:

        # Encontra todos os links de sub-tópicos dentro do tópico atual
        subtopic_links = topic.find_all("a", class_="categoryTab")

        # Itera sobre cada link de sub-tópico
        for subtopic_link in subtopic_links:

            # Extrai a URL do sub-tópico e o título
            subtopic_url = subtopic_link["href"]
            subtopic_title = subtopic_link.text.strip()

            # Faz uma nova requisição HTTP para a URL do sub-tópico e obtém o conteúdo HTML
            subtopic_response = requests.get(subtopic_url)
            subtopic_html_content = subtopic_response.content

            # Cria um novo objeto BeautifulSoup para analisar o HTML do sub-tópico
            subtopic_soup = BeautifulSoup(subtopic_html_content, "html.parser")

            # Encontra o elemento HTML que contém o conteúdo do sub-tópico
            subtopic_content_div = subtopic_soup.find("div", class_="wiki_detail_contents js-childTagMaxWidthLimit")

            # Verifica se o conteúdo do sub-tópico foi encontrado
            if subtopic_content_div:
                # Encontra todos os parágrafos dentro do sub-tópico e os junta em uma única string
                paragraphs = subtopic_content_div.find_all("p")
                subtopic_content = "\n".join([paragraph.text.strip() for paragraph in paragraphs])

                # Escreve no arquivo de texto o título e o conteúdo do sub-tópico
                txt_file.write(f"Subtópico: {subtopic_title}\n")
                txt_file.write(f"Conteúdo do Subtópico:\n{subtopic_content}\n\n")

print("Dados exportados para output.txt")
