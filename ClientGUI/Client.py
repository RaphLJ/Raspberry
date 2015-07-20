__author__ = 'Raphael'

import logging

from GUI import *
import socket
from sys import *

logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    # datefmt='%y-%m-%d %H:%M:%S:%',
                    filename = 'clientGUI.log')

logging.info('Demarrage application')

HOST = '192.168.1.50' #IP Serveur
PORT = 10000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.connect((HOST,PORT))
    logging.debug('La connection au serveur est etablie')
except socket.error:
    logging.error('La connection au serveur a echoue : ' + str(socket.error.strerror))



mainloop()
