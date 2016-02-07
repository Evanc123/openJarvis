import spotipy
import sys
import webbrowser

def song_name_to_browser(song_name):
	spotify = spotipy.Spotify()
	name = "Express Yourself"
	results = spotify.search(q='track:' + song_name, type='track')

	#print type(results)
	print results
	print results['tracks']['items'][0]['external_urls']
	webbrowser.open(results['tracks']['items'][0]['external_urls']["spotify"], new=2, autoraise=True)
