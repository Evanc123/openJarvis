import spotipy
import sys
import webbrowser
spotify = spotipy.Spotify()
name = "Express Yourself"
results = spotify.search(q='track:' + name, type='track')

#print type(results)

webbrowser.open(results['tracks']['items'][0]['external_urls']["spotify"], new=2, autoraise=True)
