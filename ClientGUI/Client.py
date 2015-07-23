__author__ = 'Raphael'

import logging

import GUI
import socket
from sys import *

def noAction(event):
    print("NO ACTION")
    pass

def buttonleftclick(event):
    logging.debug('Button LEFT click')
    sendMessage('LEFT')


def buttonrightclick(event):
    logging.debug('Button RIGHT click')
    sendMessage('RIGHT')


def buttonforwardclick(event):
    logging.debug('Button FORWARD click')
    sendMessage('FORWARD')


def buttonbackwardclick(event):
    logging.debug('Button BACKWARD click')
    sendMessage('BACKWARD')


def buttonstopclick(event):
    logging.debug('Button STOP click')
    sendMessage('STOP')


def buttontestclick(event):
    logging.debug('Button TEST click')
    GUI.buttonconnect["bg"] = "green"
    GUI.buttonconnect["text"] = "Connected"


def buttonconnectclick(event):
    logging.debug('Button CONNECT click')
    connectSocket()
    if isSocketConnected:
        GUI.buttonconnect["bg"] = "#80ff80"
        GUI.buttonconnect["text"] = "Connected"
    else:
        GUI.buttonconnect["bg"] = "red"
        GUI.buttonconnect["text"] = "Disconnected"


def connectSocket():
    global isSocketConnected
    if isSocketConnected == False:
        try:
            mySocket.connect((HOST, PORT))
            logging.debug('La connection au serveur est etablie')
            isSocketConnected = True
            enableButtons()
        except socket.error:
           logging.error('La connection au serveur a echoue : ' + str(socket.error.strerror))
           isSocketConnected = False
           disableButtons()
    else:
        mySocket.close()
        isSocketConnected = False
        disableButtons()
        logging.debug('La connection au serveur a ete interrompue')


def sendMessage(message):
    global isSocketConnected
    if isSocketConnected:
        message_encode = message.encode("utf_8")
        mySocket.send(message_encode)
        logging.debug("Message envoye : " + str(message_encode))
    else:
        logging.debug("Ce message n'a pas ete envoye : " + str(message))

def enableButtons():
    GUI.buttonleft.bind("<Button-1>", buttonleftclick)
    GUI.buttonright.bind("<Button-1>", buttonrightclick)
    GUI.buttonforward.bind("<Button-1>", buttonforwardclick)
    GUI.buttonbackward.bind("<Button-1>", buttonbackwardclick)
    GUI.buttonstop.bind("<Button-1>", buttonstopclick)

    GUI.buttonleft.config(state="normal")
    GUI.buttonright.config(state="normal")
    GUI.buttonforward.config(state="normal")
    GUI.buttonbackward.config(state="normal")
    GUI.buttonstop.config(state="normal")

def disableButtons():
    GUI.buttonleft.unbind("<Button-1>")
    GUI.buttonright.unbind("<Button-1>")
    GUI.buttonforward.unbind("<Button-1>")
    GUI.buttonbackward.unbind("<Button-1>")
    GUI.buttonstop.unbind("<Button-1>")

    GUI.buttonleft.config(state="disabled")
    GUI.buttonright.config(state="disabled")
    GUI.buttonforward.config(state="disabled")
    GUI.buttonbackward.config(state="disabled")
    GUI.buttonstop.config(state="disabled")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    # datefmt='%y-%m-%d %H:%M:%S:%',
                    filename='clientGUI.log')

logging.info('Demarrage application')

HOST = '192.168.1.100'  # IP Serveur
PORT = 10000

disableButtons()

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
isSocketConnected = False

GUI.buttonconnect.bind("<Button-1>", buttonconnectclick)

GUI.mainloop()
