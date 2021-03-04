import naoqi
from naoqi import ALProxy
import os

#IP = " 172.20.10.7"
IP = "192.168.43.218"
tts= ALProxy("ALTextToSpeech", IP , 9559 )
tts.say("\\vct=100\\hi")
tts.stopAll()
