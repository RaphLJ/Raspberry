__author__ = 'Raphael'

from tkinter import *
import logging
import tkinter as tk
import tkinter.font as tkfont

# def buttonleftclick():
#     logging.debug("Button Left Click")
#     Client.sendMessage("Left")

# def buttonrightclick():
#     logging.debug("Button Right Click")

# def buttonforwardclick():
#     logging.debug("Button Forward Click")

# def buttonbackwardclick():
#     logging.debug("Button Backward Click")

# def buttonstopclick():
#     logging.debug("Button Stop Click")

# def buttonleftrelease(event):
#     logging.debug("Button Left Released")

# def buttonleftpressed(event):
#     logging.debug("Button Left Pressed")

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

frameButton = Frame(master, width=300, height=210)
frameButton.grid(row=0, column=0)

frameStop = Frame(master, width=80, height=290)
frameStop.grid(row=0, column=1, rowspan=2)

frameBottom = Frame(master, width=300, height=80)
frameBottom.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

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

buttonconnect = Button(frameBottom, text="Connect", font=myFont)
buttonconnect.grid(row=0, column=0)

buttontest = Button(frameBottom, text="TEST", font=myFont)
buttontest.grid(row=0, column=1)