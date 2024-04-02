import re
import spotifyplaylist
from ytplaylist import run
import webbrowser

playlist_link = input("Enter Playlist link: ")

def get_playlist_id(playlist_link):
    pattern = r'playlist/([\w\d]+)'
    match = re.search(pattern, playlist_link)
    if match:
        return match.group(1)
    else:
        return None

def open_youtube_playlist(playlist_id):
    url = f"https://www.youtube.com/playlist?list={playlist_id}"
    webbrowser.open_new_tab(url)

# spotify
playlist_id = get_playlist_id(playlist_link)
playlist_name, playlist_tracks = spotifyplaylist.get_playlist_tracks(playlist_id)
# youtube
playlist_id = run(playlist_name, playlist_tracks)
open_youtube_playlist(playlist_id)
