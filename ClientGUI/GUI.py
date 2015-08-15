__author__ = 'Raphael'

from tkinter import *
import logging
import tkinter as tk
import tkinter.font as tkfont

import time
import math
import ClientGlobals

def keyboardpressed(event):
    logging.debug("Keyboard Pressed" + repr(event.char) + "(" + str(event.keycode) + ")")
    if event.keycode==81:
        logging.debug("I want to QUIT !")
        exit()

def makeMove(currentMoveType, deltaT):
    global currentPosition
    global currentXCoord
    global currentYCoord
    global currentDirection
    if (currentMoveType =="FORWARD" or currentMoveType =="BACKWARD"):
        if (currentMoveType == "FORWARD"):
            speedDirection = 1
        else:
            speedDirection = -1

        canvasRoute.itemconfigure(currentPosition, fill="blue")
        # currentPosition["fill"] = "blue"
        newXCoord = currentXCoord + linearSpeed * math.cos(currentDirection * math.pi / 180) * deltaT * speedDirection
        newYCoord = currentYCoord + linearSpeed * math.sin(currentDirection * math.pi / 180) * deltaT * speedDirection
        currentPosition= canvasRoute.create_oval(newXCoord-sizePoint,newYCoord-sizePoint,newXCoord+sizePoint,newYCoord+sizePoint, width=1, fill="red")
        currentLine = canvasRoute.create_line(currentXCoord, currentYCoord, newXCoord, newYCoord, fill="red")
        currentXCoord=newXCoord
        currentYCoord=newYCoord
        canvasRoute.update_idletasks() # Pour rafraichir l'ecran
        # time.sleep(0.5)
        # canvasRoute.itemconfigure(currentLine, fill="grey")
    if (currentMoveType=="LEFT"):
        # if (anAction.duration < 0.1):
        #     currentDirection -= 30
        # else:
            currentDirection -= angularSpeed * deltaT
    if (currentMoveType=="RIGHT"):
        # if (anAction.duration < 0.1):
        #     currentDirection += 30
        # else:
            currentDirection += angularSpeed * deltaT

def initGraph():
    global currentXCoord
    global currentYCoord
    global currentDirection
    # global speed
    global currentPosition

    currentXCoord = int(canvasRoute["width"]) / 2
    currentYCoord = int(canvasRoute["height"]) / 2
    currentDirection = -90
    # speed = 1
    # theglobals.speed = 1

    currentPosition = canvasRoute.create_oval(currentXCoord-sizePoint,currentYCoord-sizePoint,currentXCoord+sizePoint,currentYCoord+sizePoint, width=1, fill="red")

def resetGraph(event):
    canvasRoute.delete("all")
    initGraph()

master = Tk()
master.title("BotCop")
myFont = tkfont.Font(size=18)

sizePoint = 2
linearSpeed = 20
angularSpeed = 30

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

frameEmpty4 = Frame(master, width=20, height=20)
frameEmpty4.grid(row=0, column=3)

frameRoute = Frame(master, width=540, height=540, borderwidth=5, highlightbackground="#000000", highlightthickness=3)
frameRoute.grid(row=0, column=4, rowspan=5)

canvasRoute = Canvas(frameRoute, width=540, height=540, bg="white")
canvasRoute.pack(side=LEFT, expand=True, fill=BOTH)

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

canvasRoute.bind("<Double-Button-1>", resetGraph)

