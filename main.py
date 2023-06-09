import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

#TODO: to avoid encoding text

# first_solution :
# print(response.encoding) --> "ISO-8859-1"
# print(response.apparent_encoding) --> "utf-8"
# response.encoding = response.apparent_encoding
# web_text = response.text

# second_solution:
# After getting response, take response.content instead of response.text and that will be of encoding utf-8.
web_text = response.content

soup = BeautifulSoup(web_text, "html.parser")
# print(soup.prettify())

all_movies_titles = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
all_movies_titles.reverse()
# or movies = all_movies_title[::-1]
# print(all_movies_titles)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in all_movies_titles:
        file.write(f"{title}\n")
