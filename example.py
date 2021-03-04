import naoqi
from naoqi import ALProxy
import os

#IP = " 172.20.10.7"
IP = "192.168.43.218"
tts= ALProxy("ALTextToSpeech", IP , 9559 )
f = open ("test.txt","r")
line = f.readline()
tts.say("\\vct=90\\" + line)
f.close()
a =input()
if (a == "stop"):
    tts.stopAll()
