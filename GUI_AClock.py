#imorting necessary modules
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os, time, winsound

def createWidgets():
    label1 = Label(window, text="Enter the time in HH:MM - ",bg="white")
    label1.grid(row=0,column=0,padx=5,pady=5)
    
    global entry1
    entry1 = Entry(window,width=15)
    entry1.grid(row=0,column=1)
    
    label2 = Label(window, text="Enter the Message of Alarm- ",bg="white")
    label2.grid(row=1,column=0,padx=5,pady=5)
    
    global entry2
    entry2 = Entry(window,width=15)
    entry2.grid(row=1,column=1)
    
    button_1= Button(window, text="Submit",width = 10,activebackground="Yellow",command=submit)
    button_1.grid(row=2,column=1)
    
    global label3
    label3=Label(window,text="",bg="white")
    label3.grid(row=3,column=0)
#DAY 2     
def message1():
    global entry1,label3
    Alarmtimelabel = entry1.get()
    label3.config(text="The Alarm is counting....",bg="white")
    messagebox.showinfo("Alarm Clock",f"the Alarm time is: {Alarmtimelabel}")
   
	    
def submit():
    global entry1,entry2,label3
    Alarmtime = entry1.get()
    message1()
    currenttime = time.strftime("%H:%M")
    alarmmessage = entry2.get()
    print(f"The Alarm time is: {Alarmtime}")
    while Alarmtime != currenttime:
        currenttime = time.strftime("%H:%M")
        time.sleep(1)
    if Alarmtime == currenttime:
        print("Playing Alarm Sound.....")
        winsound.PlaySound("*",winsound.SND_ASYNC)
        label3.config(text="Aarm Sound Playing>>>>",bg="white")
        messagebox.showinfo("Alarm Message",f"The Message is: {alarmmessage}")     
#Tk()window           
window = tk.Tk()
window.title("My First GUI Alarm Clock")
createWidgets()
window.config(bg="white")
window.geometry("400x150")
mainloop()











