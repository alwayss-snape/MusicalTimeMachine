from urllib import response
from bs4 import BeautifulSoup
import requests

date = input("which year in music you wanna travel to? Type the date in this format\nDD-MM-YYYY: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_name_span = soup.find("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_name_span]


# ClientID = YourSpotifyClientID
# CLientSecret = YourSpotifyClientSecret

import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth
    (
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= YourSpotifyClientID,
        client_secret= YourSpotifyClientSecret,
        show_dialog=True,
        cache_path="token.txt"
        )
)
user_id = sp.current_user()["id"]
