__author__ = 'Raphael'

import time

class globalVar:
    """contains all global variables"""

    speed = 1

    def __init__(self):
        self.startTime = time.time()

    def startTiming(self, moveType):
        self.startTime = time.time()
        self.currentMoveType = moveType

    def getDeltaT(self):
        return time.time() - self.startTime