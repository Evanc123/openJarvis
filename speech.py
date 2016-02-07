import time
import threading
from subprocess import call
import webcolors
from flux_master import *
from send_sms import *
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 70)


engine.setProperty('voice', 'english')


name_to_number = {'Anders': '+17033341250'}

class Jarvis:
    def __init__(self):
        pass
    def new_query(self, result):
        if 'door' in result:

            if 'open' in result:
                thread = OpenDoorThread()
                thread.daemon = True
                thread.start()
                engine.say("Lock Opening")

            if 'close' in result:
                thread = CloseDoorThread()
                thread.daemon = True
                thread.start()
                engine.say("Lock Closing")
        if 'change' in result:
            color = result.split(' ')[-1]
            bulbmaster(color)
            engine.say("Changing to %s" % color)
        if 'text' in result:
            name = result.split(' ')[1]
            content = result.split(' ')[2:]
            content = ''.join(content)
            sendText(name_to_number[name], content)
            engine.say("Texting %s" % name)





class CloseDoorThread(threading.Thread):
    def run(self):
        '''Start your thread here'''
        call(["./close.sh"])
        pass
class OpenDoorThread(threading.Thread):
    def run(self):
        '''Start your thread here'''
        call(["./open.sh"])
        pass


J = Jarvis()

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
#ource)

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshhold = 4000
      
         # listen for 1 second to calibrate the energy threshold for ambient noise levels
        print("Say something!")
        audio = r.listen(source)

        result = ''
    # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            result = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + result)
            
        except sr.UnknownValueError:
            result = ''
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            result = ''
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        if 'Jarvis in results':
            J.new_query(result)