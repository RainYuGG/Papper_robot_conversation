import naoqi
import os
from naoqi import ALProxy
import time
while(1):
    IP = "192.168.43.218"#"172.20.10.7" #"192.168.1.124" 
    tts = ALProxy("ALTextToSpeech", IP, 9559)
    fo = open("output.txt", "r")
    line = fo.readline()
    line2 = line
    print ("line:\n" +line)
    print ("line2:\n"+line2)
    print("bf")
    f_stop = open("stop.txt","w+")
    f_stop.write("saying\n")
    time.sleep(1)
    f_stop.close()
    test = open("stop.txt","r")
    print (test.read())
    test.close()

    tts.say("\\vct=100\\" + line)

    f_stop = open("stop.txt","w+")
    f_stop.write("start\n")
    time.sleep(1)
    print(f_stop.read())
    f_stop.close()
    print("cls")
    fo.close()
    print (line == line2)
    
    while(line == line2):
        f2 = open("output.txt","r")
        line2 = f2.readline()
 #       print (line == line2)
#        print ("line2 in while = "+line2)    
        f2.close()
        time.sleep(1)

