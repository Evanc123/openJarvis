from subprocess import call
import webcolors
import re
import random
def party():
	rgbs = ["255,0,0", "0,0,255", "0,255,0", "255,100,0", "255,0,255", "0,255,255"]
	rgb =""
	random.shuffle(rgbs)
	for i in range(len(rgbs)):
		rgb+= rgbs[i]
		rgb+= " "
	#for i in range(random.randint(4,12)):
	#	color = []
	#	for x in range(3):
	#		z = random.randint(0,255)
	#		color.append(random.randint(0,255))
	#		rgb += str(z) + ","
	#	rgb += " " 
	rgb = rgb[0:len(rgb)-1]
	print rgb
	
	
	call(["python", "/home/anders/Flux_led/flux_led-master/flux_led.py", "10.0.1.4", "-C", "strobe", "99", rgb])

