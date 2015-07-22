__author__ = 'Raphael'

import logging

import GUI
import socket
from sys import *


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
    try:
        mySocket.connect((HOST, PORT))
        logging.debug('La connection au serveur est etablie')
        isSocketConnected = True
    except socket.error:
        logging.error('La connection au serveur a echoue : ' + str(socket.error.strerror))
        isSocketConnected = False


def sendMessage(message):
    message_encode = message.encode("utf_8")
    mySocket.send(message_encode)
    logging.debug("Message envoye : " + str(message_encode))


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    # datefmt='%y-%m-%d %H:%M:%S:%',
                    filename='clientGUI.log')

logging.info('Demarrage application')

HOST = '192.168.1.100'  # IP Serveur
PORT = 10000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
isSocketConnected = False

GUI.buttonleft.bind("<Button-1>", buttonleftclick)
GUI.buttonright.bind("<Button-1>", buttonrightclick)
GUI.buttonforward.bind("<Button-1>", buttonforwardclick)
GUI.buttonbackward.bind("<Button-1>", buttonbackwardclick)
GUI.buttonstop.bind("<Button-1>", buttonstopclick)
GUI.buttonconnect.bind("<Button-1>", buttonconnectclick)
GUI.buttontest.bind("<Button-1>", buttontestclick)
GUI.mainloop()
