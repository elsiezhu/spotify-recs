"""
recommend songs using spotipy and spotify api
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import get_songs
import get_categories_ids
import random

# client id and client secret id
c_id = os.environ.get('c_id')
s_id = os.environ.get('s_id')

# query api's endpoints
client_credentials_manager = SpotifyClientCredentials(client_id=c_id, client_secret=s_id)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def recommend_songs(amount: int, category: str, country: str):
    category_id = get_categories_ids.get_id(category=category)
    playlists = get_songs.get_playlists_by_id(category_id=category_id, country=country, limit=50)
    random_songs = []
    for playlist in playlists:
        while True:
            track_info = get_random_track(playlist_id=playlists[playlist], country=country)
            if track_info not in random_songs:
                break
        random_songs.append(track_info)

    recommended_songs = []
    for track_info in random_songs:
        track = track_info[0] + ' - '
        for i, artist in enumerate(track_info[1]):
            if i == 0:
                track += artist
                continue
            track += ' & ' + artist
        recommended_songs.append(track)

    return random.choices(recommended_songs, k=amount)


def get_random_track(playlist_id: str, country: str) -> list:
    tracks = get_songs.get_playlist_tracks_by_id(playlist_id=playlist_id, country=country, limit=50)
    return random.choice(tracks)
