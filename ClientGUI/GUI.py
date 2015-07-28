__author__ = 'Raphael'

from tkinter import *
import logging
import tkinter as tk
import tkinter.font as tkfont

def keyboardpressed(event):
    logging.debug("Keyboard Pressed" + repr(event.char) + "(" + str(event.keycode) + ")")
    if event.keycode==81:
        logging.debug("I want to QUIT !")
        exit()

master = Tk()
myFont = tkfont.Font(size=18)

# frame = Frame(master)
# frame.bind("<Key>", keyboardpressed)
# frame.pack()
# frame.focus_set()

frameButton = Frame(master, width=300, height=210, borderwidth=5, highlightbackground="#000000", highlightthickness=3)
frameButton.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

frameEmpty1 = Frame(master, width=300, height=20)
frameEmpty1.grid(row=1, column=0)

frameCamera = Frame(master, width=300, height=210, borderwidth=5, highlightbackground="#000000", highlightthickness=3)
frameCamera.grid(row=2, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

frameEmpty2 = Frame(master, width=300, height=20)
frameEmpty2.grid(row=3, column=0)

frameBottom = Frame(master, width=300, height=80, borderwidth=5, highlightbackground="#000000", highlightthickness=3)
frameBottom.grid(row=4, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

frameEmpty3 = Frame(master, width=20, height=20)
frameEmpty3.grid(row=0, column=1)

frameStop = Frame(master, width=80, height=290, borderwidth=5, highlightbackground="#000000", highlightthickness=3)
frameStop.grid(row=0, column=2) #, rowspan=2

buttonleft = Button(frameButton, text="Left", font=myFont)
buttonleft.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

# buttonleft.bind("<Button-1>", buttonleftpressed)
# buttonleft.bind("<ButtonRelease-1>", buttonleftrelease)

buttonright = Button(frameButton, text="Right", font=myFont)
buttonright.grid(row=1, column=2, sticky=tk.N+tk.E+tk.S+tk.W)

buttonforward = Button(frameButton, text="Forward", font=myFont)
buttonforward.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

buttonbackward = Button(frameButton, text="Backward", font=myFont)
buttonbackward.grid(row=2, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

buttonstop = Button(frameStop, text="Stop", font=myFont)
buttonstop.grid(sticky=tk.N+tk.E+tk.S+tk.W)
buttonstop["bg"]="#ff0000"
buttonstop["fg"]="#ffffff"

slidertilt=Scale(frameCamera, from_=90, to=-15, label="Tilt", sliderlength=20, length=150)
slidertilt.grid(row=0, column=0, sticky=tk.N+tk.S)

sliderpan=Scale(frameCamera, from_=-90, to=90, orient=HORIZONTAL, label="Pan", sliderlength=20, length=300)
sliderpan.grid(row=1, column=0, sticky=tk.E+tk.W)

buttonresetcamera = Button(frameCamera, text="Reset", font=myFont)
buttonresetcamera.grid(row=2, column=0)

buttonconnect = Button(frameBottom, text="Connect", font=myFont)
buttonconnect.grid(row=0, column=0)