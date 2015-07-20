__author__ = 'Raphael'

from tkinter import *
import logging

def buttonleftclick():
    logging.debug("Button Left Click")

def buttonrightclick():
    logging.debug("Button Right Click")

def buttonforwardclick():
    logging.debug("Button Forward Click")

def buttonbackwardclick():
    logging.debug("Button Backward Click")

def buttonstopclick():
    logging.debug("Button Stop Click")

def buttonleftrelease(event):
    logging.debug("Button Left Released")

def buttonleftpressed(event):
    logging.debug("Button Left Pressed")

def keyboardpressed(event):
    logging.debug("Keyboard Pressed" + repr(event.char) + "(" + str(event.keycode) + ")")
    if event.keycode==81:
        logging.debug("I want to QUIT !")
        exit()


master = Tk()

frame = Frame(master)
frame.bind("<Key>", keyboardpressed)
frame.pack()
frame.focus_set()

buttonleft = Button(frame, text="Left", command=buttonleftclick)
buttonleft.grid(row=2, column=1)

buttonleft.bind("<Button-1>", buttonleftpressed)
buttonleft.bind("<ButtonRelease-1>", buttonleftrelease)

buttonright = Button(frame, text="Right", command=buttonrightclick)
buttonright.grid(row=2, column=3)

buttonforward = Button(frame, text="Forward", command=buttonforwardclick)
buttonforward.grid(row=1, column=2)

buttonbackward = Button(frame, text="Backward", command=buttonbackwardclick)
buttonbackward.grid(row=3, column=2)

buttonstop = Button(frame, text="Stop", command=buttonstopclick)
buttonstop.grid(row=2, column=2)

