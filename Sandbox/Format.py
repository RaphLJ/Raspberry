__author__ = 'Raphael'

x=1

y='F'

print('{0:1s}{1:03d}\n'.format(y, x))
print('{0:1s}{1:03d}'.format(y, x))
print("Test !")


class maClasse:

    def __init__(self):
        self.z = 2
        self.t = "G"


    def sendCommand(self):
        command = '{0:1s}{1:03d}'.format(self.t,self.z)
        print(command)

laclasse = maClasse()
laclasse.sendCommand()