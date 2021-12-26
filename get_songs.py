"""get data from spotify api using spotipy"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# client id and client secret id
c_id = os.environ.get('c_id')
s_id = os.environ.get('s_id')

# query api's endpoints
client_credentials_manager = SpotifyClientCredentials(client_id=c_id, client_secret=s_id)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_categories(limit: int, country: str) -> dict[str, str]:
    """
    Returns a dict mapping category names to their ids
    The parameter, limit, is the amount of categories wanted

    Preconditions:
    - 1 <= limit <= 50
    """
    results = sp.categories(country=country, locale=None, limit=limit, offset=0)
    results_categories = results['categories']['items']
    categories_ids = {}
    for i in range(len(results_categories)):
        categories_ids[results_categories[i]['name']] = results_categories[i]['id']

    return categories_ids


def get_category_playlists(category: str, country: str, limit: int) -> dict[str, str]:
    categories = get_categories(limit=50, country=country)
    category_id = categories[category]
    playlists = sp.category_playlists(category_id=category_id, country=country, limit=limit, offset=0)
    playlists_names_ids = {}
    for i in range(len(playlists['playlists']['items'])):
        name = playlists['playlists']['items'][i]['name']
        playlist_id = playlists['playlists']['items'][i]['id']
        playlists_names_ids[name] = playlist_id
    return playlists_names_ids


def get_playlist_tracks(category: str, playlist_name: str, country: str, limit: int) -> list[list]:
    playlists = get_category_playlists(category=category, country=country, limit=50)
    playlist_id = playlists[playlist_name]
    tracks = sp.playlist_items(playlist_id=playlist_id, fields=None, limit=limit, offset=0, market=None)

    # iterate over each track to get track name, artists, and track id
    track_list = []
    for track in tracks['items']:
        # get name of track
        track_name = track['track']['name']

        # get a list of artist names
        artist_info = track['track']['artists']
        artists = []
        for artist in artist_info:
            artists.append(artist['name'])

        # get track id
        track_id = track['track']['id']

        # add all three to list
        track_list.append([track_name, artists, track_id])

    return track_list
