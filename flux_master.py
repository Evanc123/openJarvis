from subprocess import call
import re
import random
import os
import webcolors

def turnOff():
	call(["python", "%s/FluxScripts/flux_led.py" % os.getcwd(), "10.0.1.4", "--off"])
def changeColor(color):
	rgb = re.sub('[() ]', '', str(webcolors.name_to_rgb(color)))
	call(["python", "%s/FluxScripts/flux_led.py" % os.getcwd(), "10.0.1.4", "-c", rgb])
def turnOn():
	call(["python", "%s/FluxScripts/flux_led.py" % os.getcwd(), "10.0.1.4", "--on"])

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
	
	
	call(["python", "%s/FluxScripts/flux_led.py" % os.getcwd(), "10.0.1.4", "-C", "strobe", "99", rgb])


def strobe(color="white"):

	if color != "white":
		rgb = re.sub('[() ]', '', str(webcolors.name_to_rgb(color)))
	else:
		rgb = "255,255,255"
	call(["python", "%s/FluxScripts/flux_led.py" % os.getcwd(), "10.0.1.4", "-C", "strobe", "100", rgb])


def bulbmaster(i):
	txt = open("bulbstate.txt", "r+")
	statelist = txt.readlines()
	state = re.sub('[\n]', '', statelist[0])
	if state == "0":
		bulbstate = False
	elif state == "1":
		bulbstate = True
	else:
		print("unexpected bulb state (not 1 or 0)")


	if i == "off":
		turnOff()
		bulbstate = False

	elif i == "on":
		turnOn()
		bulbstate = True

	elif "strobe" in i:
		print 'strobe'
		if bulbstate == False:
			turnOn()
			bulbstate = True
		strobe()
	elif "party" in i:
		if bulbstate == False:
			turnOn()
			bulbstate = True
		party()


	else:
		if bulbstate == False:
			turnOn()
			bulbstate = True
		changeColor(i)


	if bulbstate:
		txt.seek(0)
		txt.write("1")
	else:
		txt.seek(0)
		txt.write("0")
	txt.close()

bulbmaster('off')
