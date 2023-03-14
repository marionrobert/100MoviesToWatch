import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_text = response.text
# print(web_text)

soup = BeautifulSoup(web_text, "html.parser")
# print(soup.prettify())

all_movies_titles = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
all_movies_titles.reverse()
# print(all_movies_titles)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in all_movies_titles:
        file.write(f"{title}\n")
