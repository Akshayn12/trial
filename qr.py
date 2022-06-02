# Import required libraries
from tkinter import *
from PIL import ImageTk, Image
import sys
import os
import subprocess
from urllib.request import urlopen 
import time
from threading import Thread
import tkinter as Tkinter


# Create an instance of tkinter window

app = Tk()
# Define the geometry of the window
app.geometry("500x500")

# def helloCallBack():
#   subprocess.run("python main.py")#creationflags=subprocess.CREATE_NEW_CONSOLE

# app.wait_visibility()
# helloCallBack()
# Thread(target=helloCallBack).start()

frame1 = LabelFrame(app, text="QR CODE", bg="white", width=500,height=500)
img = ImageTk.PhotoImage(Image.open("rrrr.png"))
label = Label(frame1, image = img)
label.pack()
frame1.grid(row=0, column=0)
frame2 = LabelFrame(app, text="Staff Detail", bg="yellow", width=1000, height=1000)
frame2.grid(row=0, column=3)
l1 = Label(frame2, text = "Name of the Employee")
l1.grid(row = 0, column = 3, sticky = W, pady = 2)

l2 = Label(frame2, text = "Punching Time")
l2.grid(row = 1, column = 3, sticky = W, pady = 2)

e1 = Entry(frame2)
e2 = Entry(frame2)

e1.grid(row = 0, column = 4, pady = 2)
e2.grid(row = 1, column = 4, pady = 2)



app.mainloop()

