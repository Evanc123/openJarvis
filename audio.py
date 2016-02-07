import pyglet
import pyglet.media as media
def main():
    fname='/home/evan/Desktop/openJarvis/openJarvis/speech/tdfw.mp3'
    src=media.load(fname)
    player=media.Player()
    player.queue(src)
    player.volume=1.0
    player.play()
    try:
        pyglet.app.run()
    except KeyboardInterrupt:
        player.next()

if __name__=="__main__":
    main()