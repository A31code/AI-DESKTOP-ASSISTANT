

#this code is owned by ayush agarwal.

import pyttsx3

def text_to_speech(text):
  #text = "hello"
  engine = pyttsx3.init()
  voice = engine.getProperty('voices')
  engine.setProperty('voice', voice[1].id)
  rate = engine.getProperty('rate')
  engine.setProperty('rate' , 'rate-10') 
  engine.say(text)
  engine.runAndWait()



#text_to_speech("hello hubby. i am really horny. can we have sex right now")