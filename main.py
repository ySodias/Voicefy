import os

from Auth import Auth
from Voice import Voice

auth = Auth(os.getenv('USERNAME'), os.getenv('SCOPE'))
voice = Voice(frase=None, audio=None)

print("Say a playlist name: ")
playlist_name = voice.ouvir_microfone()

print("Say a playlist description: ")
playlist_description = voice.ouvir_microfone()

auth.post_playlist(playlist_name, playlist_description)

print("Say a music name: ")
nome_musica = voice.ouvir_microfone()

print(nome_musica)

result = auth.get_music_from_spotify(nome_musica)

print(result)


