import pyglet

def play(song="kpdarkhorse.mp3"):
	print("Now Playing " + song)

	#Load the song into memory
	music = pyglet.resource.media(song)
	music.play()

	#Start the decoding of the song and play it
	pyglet.app.run()

