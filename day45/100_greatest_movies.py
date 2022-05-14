"""
make a list of 100 greatest movies from IMDb article
"""

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.imdb.com/list/ls055592025/")

soup = BeautifulSoup(response.text, "html.parser")

n = 1
with open("movies.txt", "w", encoding="utf-8") as f:
    for title in soup.select(selector="h3 a"):
        f.write(f"{n}) {title.text}\n")
        n += 1
