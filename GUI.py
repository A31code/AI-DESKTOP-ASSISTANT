
#this code is owned by ayush agarwal.


from tkinter import *
from PIL import Image , ImageTk
import speechtext
import action
root = Tk()
root.title("AI.TECH")
root.geometry("550x675")
root.resizable(False , False)
root.config(bg="#6F8FAF")

#ASK FUNCTION

def ask():
  user_val = speechtext.speech_to_text()
  bot_val = action.action(user_val)
  text.insert(END , "AYUSH-->" + user_val + "\n")
  if bot_val != None:
    text.insert(END , "SIFRA <--" + str(bot_val)+"\n")
  if bot_val == "ok ayush":
    root.destroy()

def send():
  send = entry.get()
  bot = action.action(send)
  text.insert(END , "AYUSH-->" + send + "\n")
  if bot != None:
    text.insert(END , "SIFRA <--" + str(bot)+"\n")
  if bot == "ok ayush":
    root.destroy()

def delete():
  text.delete('1.0' , "end")




#FRAME

frame = LabelFrame(root , padx= 100 , pady= 7 , borderwidth= 3 , relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row = 0 , column = 1, padx = 60 , pady = 10)

#FRAME_LABEL

text_label = Label(frame , text="SIFRA" , font=("Algerian" , 22 , "bold") , bg="#3F4FAF")
text_label.grid(row = 0 , column = 0 , padx = 60 , pady = 20)


#IMAGE_LABEL
image = ImageTk.PhotoImage(Image.open("image/assistant.jpg"))
image_label= Label(frame , image=image)
image_label.grid(row = 1, column = 0 , pady = 20)


#ADDING A TEXT WIDGET

text = Text(root , font=('Algerian 14 bold') , bg="#3F4FAF")
text.grid(row= 2 , column= 0)
text.place(x= 100 , y= 375 , width= 375 , height= 100)

#ENTRY WIDGET

entry = Entry(root, justify=CENTER)
entry.place(x= 100 , y= 500, width= 350, height= 30)


#BUTTON CREATION

Button1 = Button(root, text="ASK" , bg= "#3F4FAF", pady= 16, padx= 40, borderwidth= 3, relief= SOLID, command=ask)
Button1.place(x= 70, y= 575)

Button2 = Button(root, text="SEND" , bg= "#3F4FAF", pady= 16, padx= 40, borderwidth= 3, relief= SOLID, command=send)
Button2.place(x= 400, y= 575)

Button3 = Button(root, text="DELETE" , bg= "#3F4FAF", pady= 16, padx= 40, borderwidth= 3, relief= SOLID, command=delete)
Button3.place(x= 225, y= 575)





root.mainloop()