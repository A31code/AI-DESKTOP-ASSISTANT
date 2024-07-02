#this code is owned by ayush agarwal.



import text_to_speech
import speechtext
import datetime
import webbrowser
import weather

def action(data):
  user_data = data.lower()
  if "what is your name" in user_data:
    text_to_speech.text_to_speech("my name is SIFRA, a member of A.I.TECH COMPANY.")
    return "my name is A.I.Tech, member SIFRA"
  
  elif "what is aitech" in user_data or "aitech?" in user_data:
      text_to_speech.text_to_speech("AITECH is a company which designs ai desktop assistance for it's customer.")
      return "AITECH is a company which designs ai desktop assistance for it's customer."
 
  elif "hello" in user_data or "hi" in user_data:
      text_to_speech.text_to_speech("hello ayush, how can i help you today?")
      return "hello ayush, how can i help you today?"

  elif "good morning" in user_data:
      text_to_speech.text_to_speech("good morning, ayush")
      return "good morning, ayush"

  elif "good afternoon" in user_data:
      text_to_speech.text_to_speech("good afternoon, ayush")
      return "good afternoon, ayush"

  elif "good evening" in user_data:
      text_to_speech.text_to_speech("good evening, ayush")
      return "good evening, ayush"

  elif "good night" in user_data:
      text_to_speech.text_to_speech("good night, ayush. sweat dreams.")
      return "good night, ayush. sweat dreams."

  elif "time now" in user_data:
      current_time = datetime.datetime.now()
      Time = (str)(current_time) + "hour :" , (str)(current_time.minute) + "minute"
      text_to_speech.text_to_speech(Time)
      return Time

  elif "shutdown" in user_data:
      text_to_speech.text_to_speech("ok ayush")
      return "ok ayush"

  elif "open youtube" in user_data:
      webbrowser.open("https://www.youtube.com/")
      text_to_speech.text_to_speech("opening youtube, ayush")
      return "opening youtube, ayush"

  elif "open google" in user_data:
      webbrowser.open("https://www.google.com/")
      text_to_speech.text_to_speech("opening google, ayush")
      return "opening google, ayush"

  elif "open whatsapp" in user_data:
      webbrowser.open("https://web.whatsapp.com/")
      text_to_speech.text_to_speech("opening whatsapp, ayush")
      return "opening whatsapp, ayush"
  

  elif "open mail" in user_data:
      webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
      text_to_speech.text_to_speech("opening mail, ayush")
      return "opening mail, ayush"

  elif "cit" in user_data:
      webbrowser.open("https://www.citranchi.ac.in/")
      text_to_speech.text_to_speech("opening cit official website home page, ayush")
      return "opening cit official website home page, ayush"

  
  elif "weather" in user_data:
      ans = weather.weather()
      text_to_speech.text_to_speech(ans)
      return ans

  elif "task" in user_data:
      text_to_speech.text_to_speech("i can do many task which are programed in me by my lovely creator ayush.")
      text_to_speech.text_to_speech("these tasks includes:")
      text_to_speech.text_to_speech("youtube, google, mail, whatsapp, cit official website, weather of ranchi, etc.")
      return "youtube, google, mail, whatsapp, cit official website, weather of ranchi, etc."

  elif "my site" in user_data:
      webbrowser.open("https://ayushagarwal.free.site.pro/")
      text_to_speech.text_to_speech("opening the site of my company, ayush")
      return "opening the site created by you, ayush"
  
  elif "os book" in user_data:
      webbrowser.open("file:///C:/Users/USER/Desktop/extras/OS%20BOOK.pdf")
      text_to_speech.text_to_speech("opening os book, ayush")
      return "opening os book, ayush"
  
  elif "dsa book" in user_data:
      webbrowser.open("file:///C:/Users/USER/Desktop/extras/DSABOOK.pdf")
      text_to_speech.text_to_speech("opening dsa book, ayush")
      return "opening dsa book, ayush"
  
  elif "copilot" in user_data:
      webbrowser.open("https://copilot.microsoft.com/?FORM=undexpand&")
      text_to_speech.text_to_speech("opening copilot, ayush")
      return "opening copilot, ayush"
  else:
      text_to_speech.text_to_speech("please say it once again, ayush")
      return "please say it once again, ayush"

   
      