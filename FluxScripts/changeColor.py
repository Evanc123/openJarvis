from subprocess import call
import webcolors
import re

def changeColor(color):
	rgb = re.sub('[() ]', '', str(webcolors.name_to_rgb(color)))
	call(["python", "/home/anders/Flux_led/flux_led-master/flux_led.py", "10.0.1.4", "-c", rgb])

