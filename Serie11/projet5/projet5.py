import requests
from bs4 import BeautifulSoup
import sqlite3

def scraper(url: str):
    conn = sqlite3.connect("articles.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles (titre TEXT, lien TEXT)''')

    page = 1
    while True:
        response = requests.get(f"{url}?page={page}")
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, "html.parser")
        articles = []
        for article in soup.find_all("article"):
            titre = article.find("h2").text.strip() if article.find("h2") else "Titre inconnu"
            lien = article.find("a")["href"] if article.find("a") else "#"
            articles.append((titre, lien))

        c.executemany("INSERT INTO articles VALUES (?, ?)", articles)
        conn.commit()
        print(f"Page {page} extraite.")
        page += 1

    conn.close()

if __name__ == "__main__":
    scraper("https://example.com")