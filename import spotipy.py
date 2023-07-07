import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Enter your Spotify API details
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'your_redirect_uri'

# Enter your user details
username = 'your_username'
playlist_id_to_copy = 'id_of_playlist_you_want_to_copy'
playlist_id_to_paste = 'id_of_playlist_where_you_want_to_paste'

# Create OAuth object
scope = 'playlist-modify-public'  # permission needed to add to new playlist
auth_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, 
                            redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope, username=username)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Get tracks from the playlist you want to copy
source_tracks = sp.playlist_items(playlist_id_to_copy)['items']
source_track_ids = [track['track']['id'] for track in source_tracks]

# Copy tracks to the target playlist
sp.playlist_add_items(playlist_id_to_paste, source_track_ids)
