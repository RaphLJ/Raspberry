__author__ = 'Raphael'

import logging
import socket
import PiRobot
from sys import *

logging.basicConfig(level=logging.DEBUG,
                    format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    # datefmt='%y-%m-%d %H:%M:%S:%',
                    filename = 'server.log')

logging.info('Demarrage application')

HOST = '192.168.1.50'
PORT = 10000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# robot.goForward()
# robot.goLeft()

try:
    mySocket.bind((HOST,PORT))
except socket.error:
    logging.error('La connection a echoue : ' + str(socket.error.strerror))
    exit()

robot = PiRobot.PiRobot()

while 1:
    mySocket.listen(2)

    connexion, adresse = mySocket.accept()
    logging.debug('La connection est etablie : ' + str(adresse[0]) + ' ' + str(adresse[1]))

    while 1:
        message_encode=connexion.recv(1024)
        message=message_encode.decode("utf_8")
        if len(message) != 0:
            logging.debug('Message recu : ' + message)
            if message=="LEFT":
                robot.goLeft()
            if message=="FORWARD":
                robot.goForward()
            if message=="RIGHT":
                robot.goRight()
            if message=="BACKWARD":
                robot.goBackward()
            if message=="STOP":
                robot.stop()
            if message[:3]=="PAN":
                robot.cameraPan()
            if message[:4]=="TILT":
                robot.cameraTilt()