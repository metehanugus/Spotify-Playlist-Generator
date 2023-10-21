import spotipy
import openai
from dotenv import dotenv_values
import pprint


config = dotenv_values("D:\GPTProjects\.env")
openai.api_key = config["OPENAI_API_KEY"]

sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id=config["SPOTIFY_CLIENT_ID"],
        client_secret=config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri="http://localhost:9999"
    )
)

current_user = sp.current_user()

assert current_user is not None

search_results = sp.search(q="Uptown Funk", type="track", limit=10)
pprint.pprint(search_results["tracks"]["items"][0]["id"])