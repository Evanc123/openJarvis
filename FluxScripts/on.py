from subprocess import call

def turnOn():
	call(["python", "/home/anders/Flux_led/flux_led-master/flux_led.py", "10.0.1.4", "--on"])
