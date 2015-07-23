__author__ = 'Raphael'

import logging
import socket
from sys import *

logging.basicConfig(level=logging.DEBUG,
                    format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    # datefmt='%y-%m-%d %H:%M:%S:%',
                    filename = 'server.log')

logging.info('Demarrage application')

HOST = '192.168.1.100'
PORT = 10000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.bind((HOST,PORT))
except socket.error:
    logging.error('La connection a echoue : ' + str(socket.error.strerror))
    exit()

while 1:
    mySocket.listen(2)

    connexion, adresse = mySocket.accept()
    logging.debug('La connection est etablie : ' + str(adresse[0]) + ' ' + str(adresse[1]))

    while 1:
        message_encode=connexion.recv(1024)
        message=message_encode.decode("utf_8")
        if len(message) != 0:
            logging.debug('Message recu : ' + message)

