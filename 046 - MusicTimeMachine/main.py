import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pprint import pprint

load_dotenv()

spotify_client = os.getenv("spotify_client")
spotify_password = os.getenv("spotify_password")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=spotify_client,
        client_secret=spotify_password,
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]

print("Welcome to the music Time Machine!\nWhich date do you wish to review?\n")
user_year = input("Please specify the year (4 digits):\n")
user_month = input("Please specify the month (2 digits):\n")
user_day = input("Please specify the day (2 digits):\n")

url = f"https://www.billboard.com/charts/hot-100/{user_year}-{user_month}-{user_day}"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

songs = soup.select(selector="li ul li h3")
song_titles = [song.getText().strip() for song in songs]
pprint(song_titles)

song_uris = []
for song in song_titles:
    result = sp.search(q=f"song:{song} year:{user_year}", type="track")
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{user_year}'s Billboard 100", public=False
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
