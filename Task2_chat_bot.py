import random
from tkinter import *
root = Tk()
root.title('Chat Bot')
root.configure(bg='brown')
root.geometry('700x660')
root.resizable(False,False)
scroll_bar = Scrollbar(root)
  
scroll_bar.pack( side = RIGHT,
                fill = Y )
txt=Text(root)
txt.configure(bg='grey',fg='black',font=('Times New Roman',12,'bold'),yscrollcommand= scroll_bar.set,height=30)




def send():
    send="You :"+ e.get()
    txt.insert(END,"\n "+send)

    if(e.get()=="hello")or(e.get()=="hii") or (e.get()=="hey") or (e.get()=="hi"):
        greeting1=['hey !' ,'hi !','hello']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting1))

    elif(e.get()=="how are you?")or(e.get()=="how's it going?") or (e.get()=="how do you do?"):
        greeting2=['good ! what about you?','I am good and you ?','fine, thankyou']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting2))

    elif(e.get()=="I am also fine")or(e.get()=="fine") or (e.get()=="good"):
        greeting0=['How may i help you?','what can i do for you ?']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting0))

    elif(e.get()=="how was your day"):
        greeting5=['it was good , what about you']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting5))

    elif(e.get()=="it was great")or(e.get()=="great")or(e.get()=="mine was also good"):
        greeting5=['awesome','nice']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting5))    

    elif(e.get()=="tell me a joke")or(e.get()=="joke"):
        greeting5=['One joke, coming up! What is a sea monster’s favorite snack? Ships and dip.','This might make you laugh. How do robots eat guacamole? With computer chips']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting5)) 

    elif(e.get()=="nice talking to you")or(e.get()=="okay good day"):
        greeting5=['same, have a nice day.']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting5))          

    elif(e.get()=="I am also good") or (e.get()=='good') or (e.get()=="fine") or (e.get()=="great"):
        greetings=['how can i help you?','what can i do for you?']
        txt.insert(END,"\n"+"Bot : "+random.choice(greetings))

    elif(e.get()=="good morning") or (e.get()=='morning'):
        greeting3=['good morning','morning ! have a great day','good day']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting3))

    elif(e.get()=="good night") or (e.get()=='night'):
        greeting4=['good night','night ! have a nice sleep']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting4))

    elif(e.get()=="good evening"):
        greeting5=['good evening']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting5))

    elif(e.get()=="good afternoon") or (e.get()=='afternoon'):
        greeting6=['good afternoon','afternoon']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting6))

    elif(e.get()=="what is your name?") or (e.get()=="who are you?"):
        intro=['My name is james.','I am bot.','Roman.']
        txt.insert(END,"\n"+"Bot : "+random.choice(intro))

    elif(e.get()=="what are you?"):
        origin=['I am a chat bot','chat bot']
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))

    elif(e.get()=="namaste") or (e.get()=="namaskaar"):
        origin=['namaste','namaskaar']
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))

    elif(e.get()=="bye") or (e.get()=='goodbye') or (e.get()=="see you") :
        greetings=['bye','goodbye','see you','have a great day']
        txt.insert(END,"\n"+"Bot : "+random.choice(greetings))

    else:
        txt.insert(END,"\n"+ "Bot : sorry, I didn't get it. I am still learning ")
    e.delete(0,END)
    
txt.pack()
scroll_bar.config(command=txt.yview)

def clear():
    txt.delete('1.0',END)
e=Entry(root,width=24,font=('Times New Roman',16))
e.place(x=120,y=600)
send=Button(root,width=8,text='send',bg='yellow',fg='black',command=send,font=('Times New Roman',14))
send.place(x=420,y=600)
clear=Button(root,width=8,text='delete',bg='yellow',fg='black',command=clear,font=('Times New Roman',14))
clear.place(x=520,y=600)

root.mainloop()
