__author__ = 'Raphael'

import serial
import logging

class PiRobot:

    def __init__(self):
        self.ser=serial.Serial('/dev/ttyUSB0', 9600)
        self.leftMotorDir = "F"
        self.leftMotorSpeed = 0
        self.rightMotorDir = "F"
        self.rightMotorSpeed = 0

    def __del__(self):
        self.ser.close()

    def sendCommand(self):

        command = '{0:1s}{1:03d}{2:1s}{3:03d}\n'.format(self.leftMotorDir, self.leftMotorSpeed, self.rightMotorDir, self.rightMotorSpeed)

        logging.debug("Commande a envoyer :" + command)
        self.ser.write(command.encode())
        self.ser.flushInput()

    def goForward(self):
        logging.debug("Go Forward")
        self.leftMotorDir = "F"
        self.leftMotorSpeed = 180
        self.rightMotorDir = "F"
        self.rightMotorSpeed = 180
        self.sendCommand()

    def goLeft(self):
        logging.debug("Go Left")
        self.leftMotorDir = "B"
        self.leftMotorSpeed = 80
        self.rightMotorDir = "F"
        self.rightMotorSpeed = 80
        self.sendCommand()

    def goRight(self):
        logging.debug("Go Right")
        self.leftMotorDir = "F"
        self.leftMotorSpeed = 80
        self.rightMotorDir = "B"
        self.rightMotorSpeed = 80
        self.sendCommand()

    def goBackward(self):
        logging.debug("Go Backward")
        self.leftMotorDir = "B"
        self.leftMotorSpeed = 180
        self.rightMotorDir = "B"
        self.rightMotorSpeed = 180
        self.sendCommand()

    def stop(self):
        logging.debug("Stop")
        self.leftMotorDir = "F"
        self.leftMotorSpeed = 0
        self.rightMotorDir = "F"
        self.rightMotorSpeed = 0
        self.sendCommand()

    def cameraPan(self):
        logging.debug("CameraPan")

    def cameraTilt(self):
        logging.debug("CameraTilt")




