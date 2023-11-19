import requests
from bs4 import BeautifulSoup

url = "https://www.naeu.playblackdesert.com/en-US/Wiki"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

topics = soup.find_all("li", class_="list_wrap show active")

with open("output.txt", mode="w", encoding="utf-8") as txt_file:
    for topic in topics:
        topic_title = topic.find("h2").text.strip()
        subtopic_links = topic.find_all("a", class_="categoryTab")

        for subtopic_link in subtopic_links:
            subtopic_url = subtopic_link["href"]
            subtopic_title = subtopic_link.text.strip()

            subtopic_response = requests.get(subtopic_url)
            subtopic_html_content = subtopic_response.content

            subtopic_soup = BeautifulSoup(subtopic_html_content, "html.parser")

            subtopic_content_div = subtopic_soup.find("div", class_="wiki_detail_contents js-childTagMaxWidthLimit")

            if subtopic_content_div:
                paragraphs = subtopic_content_div.find_all("p")
                subtopic_content = "\n".join([paragraph.text.strip() for paragraph in paragraphs])

                txt_file.write(f"Subtópico: {subtopic_title}\n")
                txt_file.write(f"Conteúdo do Subtópico:\n{subtopic_content}\n\n")

print("Dados exportados para output.txt")
