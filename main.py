from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root=Tk()
root.title("Game")
root.configure(background="purple")


#picture
rock_img=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor.jpg"))
rock_img_comp=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("scissor.jpg"))


#insert picture
user_label = Label(root,image=scissor_img,bg="purple")
comp_label = Label(root,image=scissor_img,bg="purple")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)


#scores

player_score=Label(root,text=0,font=100,bg="purple",fg="white")
computer_score=Label(root,text=0,font=100,bg="purple",fg="white")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)


#indicators
user_indicator = Label(root,font=50,text="USER",bg="purple",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="purple",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)


#messages

msg=Label(root,font=50,bg="purple",fg="white")
msg.grid(row=3,column=2)


#update message
def updatemessage(x):
    msg["text"]=x


#update  score
def updateuserscore():
    score=int(player_score["text"])
    score+=1
    player_score["text"]=str(score)

def updatecompscore():
    score=int(computer_score["text"])
    score+=1
    computer_score["text"]=str(score)



#check winner

def checkwin(player,computer):
    if player == computer:
        updatemessage("Its a tie!!!!")
    elif player == "rock":
        if computer=="paper":
            updatemessage("You Loose")
            updatecompscore()
        else:
            updatemessage("You Win")
            updateuserscore
    elif player=="paper":
        if computer=="scissor":
            updatemessage("You Loose")
            updatecompscore()
        else:
            updatemessage("You Win")
            updateuserscore()
    elif player=="scissor":
        if computer=="rock":
            updatemessage("You Loose")
            updatecompscore()
        else:
            updatemessage("You Win")
            updateuserscore()
    else:
        pass

#update choice


choices=["rock","paper","scissor"]
def updatechoices(x):


#for computer
  
    compchoice=choices[randint(0,2)]
    if compchoice=="rock":
       comp_label.configure(image=rock_img_comp)
    elif compchoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)



#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    
    checkwin(x,compchoice)

#button

rock = Button(root,width=20,height=2,text="ROCK",bg="red",fg="white",command=lambda:updatechoices("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="green",fg="white",command=lambda:updatechoices("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="blue",fg="white",command=lambda:updatechoices("scissor")).grid(row=2,column=3)

root.mainloop()