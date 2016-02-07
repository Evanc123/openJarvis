from changeColor import changeColor
from off import turnOff
from on import turnOn
from strobe import strobe
from party import party
from subprocess import call
import re


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