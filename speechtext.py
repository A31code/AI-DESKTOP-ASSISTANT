
#this code is owned by ayush agarwal.

import speech_recognition as sr
#import pyaudio
#from distutils.version import LooseVersion

def speech_to_text():
  r = sr.Recognizer()
  #self.pyaudio_module = self.get_pyaudio()
  with sr.Microphone() as source:
    audio = r.listen(source)
  try:
    voice_data= ""
    voice_data = r.recognize_google(audio)
    return voice_data
  except sr.UnknownValueError:
    print("error")
  except sr.RequestError:
    print("REQUEST_ERROR")

  
#speech_to_text()  
  
  