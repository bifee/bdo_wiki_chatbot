import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.naeu.playblackdesert.com/en-US/Wiki"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

topics = soup.find_all("li", class_="list_wrap show active")

with open("output.csv", mode="w", encoding="utf-8", newline="") as csv_file:

    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["Tópico", "Subtópico", "URL", "Conteúdo"])

    for topic in topics:

        topic_title = topic.find("h2").text.strip()

        subtopic_links = topic.find_all("a", class_="categoryTab")  # Substitua "categoryTab" pela classe real do link

        for subtopic_link in subtopic_links:
            subtopic_url = subtopic_link["href"]
            subtopic_title = subtopic_link.text.strip()

            subtopic_response = requests.get(subtopic_url)
            subtopic_html_content = subtopic_response.content

            subtopic_soup = BeautifulSoup(subtopic_html_content, "html.parser")

            subtopic_content_div = subtopic_soup.find("div", class_="wiki_detail_contents js-childTagMaxWidthLimit")

            if subtopic_content_div:
                paragraphs = subtopic_content_div.find_all("p")
                subtopic_content = " ".join([paragraph.text.strip().replace("\n", " ") for paragraph in paragraphs])

                # print(f"Tópico: {topic_title}, Subtópico: {subtopic_title}")
                # print(f"Conteúdo do Subtópico:\n{subtopic_content}")
                # print("-" * 50)

                csv_writer.writerow([topic_title, subtopic_title, subtopic_url, subtopic_content])

print("Dados exportados para output.csv")
