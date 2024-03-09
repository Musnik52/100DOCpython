import requests
# from pprint import pprint
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")


titles = soup.find_all(name="h3", class_="title")
movies = [title.getText() for title in titles]
with open("./movies.txt", "w", encoding="utf8") as file:
    for movie in movies[::-1]:
        # pprint(movie)
        file.write(f"{movie}\n")
