# Pepper_robot_conversation

## Requirement 
1. python2
2. python3
3. google-cloud-speech
4. SpeechRecongition
5. Portaudio
6. Pyaudio
7. Dialogflow
8. NAOqi

## SETTING:

set the PATH in ".bashrc"

export PYTHONPATH=${PYTHONPATH}:/PATH/to/pynaoqi-python2.7-2.5.5.5-linux64/lib/python2.7/site-packages

export QI_SDK_PREFIX=/PATH/to/pynaoqi-python2.7-2.5.5.5-linux64

### Set your own Q&A in dialogflow and export to ".json" file

export GOOGLE_APPLICATION_CREDENTIALS=/PATH/to/(your own dialogflow json file).json




## TEST:

python example.py (text if NAOqi is installed;need to connect Pepper)



## STEP:


1. python3 speech_recongnition.py 
2. python3 dddialogflow.py
3. python opentxt_robot_say_.py
