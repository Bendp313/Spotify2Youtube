import os
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from ids import YT_API
API_KEY = YT_API

def authenticate_youtube():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes = ["https://www.googleapis.com/auth/youtube"])
    flow.run_local_server(port=8888, prompt="consent", authorization_prompt_message="")
    credentials = flow.credentials
    return credentials

def create_playlist(youtube, title):
    request = youtube.playlists().insert(
        part="snippet",
        body={
          "snippet": {
            "title": title,
          }
        }
    )
    response = request.execute()
    return response['id']

def playlistadd(youtube, tracks, playlistid):
    for track in tracks:
        #video search
        search_response = youtube.search().list(
            q=f"{track['name']} {track['artists']}",
            part='id',
            type='video',
            maxResults=1
        ).execute()
        # get video ID
        video_id = search_response['items'][0]['id']['videoId']
        # add to playlist
        playlist_items_insert_response = youtube.playlistItems().insert(
            part='snippet',
            body={
                'snippet': {
                    'playlistId': playlistid,
                    'position': 0,
                    'resourceId': {
                        'kind': 'youtube#video',
                        'videoId': video_id
                    }
                }
            }
        ).execute()

def run(playlist_name, playlist_tracks):
    credentials = authenticate_youtube()
    youtube = build(serviceName='youtube',version='v3', credentials= credentials)
    playlistid = create_playlist(youtube, playlist_name)
    playlistadd(youtube, playlist_tracks, playlistid)
    return playlistid

    
    
    
