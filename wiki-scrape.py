import requests
from bs4 import BeautifulSoup

url = "https://www.naeu.playblackdesert.com/en-US/Wiki"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

topics = soup.find_all("li", class_="list_wrap show active")

for topic in topics:

    topic_title = topic.find("h2").text.strip()

    print(f"Tópico: {topic_title}")

    subtopic_links = topic.find_all("a", class_="categoryTab")  # Substitua "subtopico-classe-link" pela classe real do link

    for subtopic_link in subtopic_links:
        subtopic_url = subtopic_link["href"]
        subtopic_title = subtopic_link.text.strip()

        subtopic_response = requests.get(subtopic_url)
        subtopic_html_content = subtopic_response.content


        subtopic_soup = BeautifulSoup(subtopic_html_content, "html.parser")

        paragraphs = subtopic_soup.find_all("p")
        subtopic_content = "\n".join([paragraph.text.strip() for paragraph in paragraphs])

        print(f"Subtópico: {subtopic_title}")
        print(f"Conteúdo do Subtópico:\n{subtopic_content}")
        print("-" * 50)
