import spotipy
from ids import CLIENT_ID, CLIENT_SECRET
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_tracks(playlist_id):
    # spotipy client
    #put client id as CLIENT_ID and client secret as CLIENT_SECRET
    client_credentials_manager = SpotifyClientCredentials(client_id= CLIENT_ID, client_secret = CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # playlist info
    playlist = sp.playlist(playlist_id)
    name = playlist['name']
    playlist_tracks = sp.playlist_tracks(playlist_id)
    # get track names and artists
    tracks = []
    for item in playlist_tracks['items']:
        track = item['track']
        track_name = track['name']
        artists = [artist['name'] for artist in track['artists']]
        tracks.append({'name': track_name, 'artists': artists})

    return name, tracks