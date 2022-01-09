import spotipy

from spotipy.oauth2 import SpotifyOAuth

class Auth:

    def __init__(self, username, scope):
        self.username = username
        self.scope = scope
        self.__spotifyObject = spotipy.Spotify(auth_manager=Auth.get_token_spotify(self))

    def get_token_spotify(self):
        return SpotifyOAuth(scope=self.scope, username=self.username)

    def post_playlist(self, playlist_name, playlist_description):
        try:
            self.__spotifyObject.user_playlist_create(user=self.username, name=playlist_name, public=True,
                                              description=playlist_description)
            return 'The Playlist was created', 201
        except ValueError as err:
            return err, type(err)

    def get_music_from_spotify(self, music):
        result = self.__spotifyObject.search(q=music)
        return {
            "name": result['tracks']['items'][00]['name'],
            "artist": result['tracks']['items'][00]['artists'][0]['name'],
            "link_music": result['tracks']['items'][00]['href'],
            "album": result['tracks']['items'][00]['album']['name'],
            "data": result['tracks']['items'][00]['album']['release_date']
        }