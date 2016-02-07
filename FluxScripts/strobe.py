from subprocess import call
import webcolors
import re
def strobe(color="white"):

	

	if color != "white":
		rgb = re.sub('[() ]', '', str(webcolors.name_to_rgb(color)))
	else:
		rgb = "255,255,255"
	call(["python", "/home/anders/Flux_led/flux_led-master/flux_led.py", "10.0.1.4", "-C", "strobe", "100", rgb])

