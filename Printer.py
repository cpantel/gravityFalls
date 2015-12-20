import sys
import os
from Statistical import *
from CaesarCipher import *
from AtbashCipher import *

class Printer(object):
    def __init__(self):

    def setCols(self):      # driver
#         tty = subprocess.Popen('stty size', 'r')

         tty = os.popen('stty size', 'r')
         rows, columns = tty.read().split()
         self.colWidth = (int(columns) - 4) / 2

    def showMessages(self):  #driver
        idx=0
        while idx * self.colWidth < len(self.ciphertext): 
            sys.stdout.write( self.ciphertext[idx * self.colWidth :(idx * self.colWidth) + self.colWidth])
            times = len(self.ciphertext) / ( idx + 1 )
            if times < self.colWidth:
                spaces = ' ' * ( 4 + self.colWidth - (len(self.ciphertext) - idx * self.colWidth ) )
            else:
                spaces = ' ' * 4
                     
            sys.stdout.write( spaces )
            sys.stdout.write( self.cleartext[idx * self.colWidth :(idx * self.colWidth)  + self.colWidth])
            print
            idx = idx + 1

    def outputLine(self,text): #driver
        if len(self.buffer) + len(text) > (self.colWidth * 2 ) + 1:
            self.flush()
        else:
            self.buffer += text + " "

    def flush(self): #driver
        if len(self.buffer) != 0:
            print(self.buffer)
            self.buffer = ""

    def accept(self):
        command = raw_input('?: ')             
        self.setCols()
        if command == 'q' or command == 'quit':
            self.exit = True
        elif command == '' or command[0:1] == 'm':
            self.showMessages()
        elif command[0:1] == 'd':
            self.showDic()
        elif command[0:2] == 'f1':
            self.showFrequencies1()
        elif command[0:2] == 'f2':
            self.showFrequencies2()
        elif command[0:2] == 'f3':
            self.showFrequencies3()
        elif command[0:1] == 'f':
            self.showFrequencies()
        elif command[0:1] == 'c': 
            self.setCols()  # command[1:5]
        elif command == 'a' or command == 'autoCol':
            self.stats.toggleAutoCol()
        elif command[0:4] == 'set ':
            if command[6:7]:
                self.dic[command[4:5]] = command[6:7]
            else:
                self.dic[command[4:5]] = '?'
            self.decrypt()
        elif command[0:9] == 'setSpace ':
            if command[9:10]:
                self.dic[command[9:10]] = " "
                self.stats.spacing = command[9:10]
            else:
                self.dic[command[9:10]] = '?'
                self.stats.spacing = False
            self.calculateFreq()
            self.decrypt()
        elif command == 's' or command == 'show':
            self.show()
        elif command == 'try Caesar':
            caesarCipher =  CaesarCipher()
            caesarCipher.tryAll(self.ciphertext)
        elif command == 'try Atbash':
            atbashCipher =  AtbashCipher()
            atbashCipher.run(self.ciphertext)
        elif command == 'ascii':
           lowerLimit = ord("a")
           upperLimit = ord("z")        
           offset = - 32

           for pos in range(lowerLimit, upperLimit):
              print pos + offset, chr(pos + offset), repr(pos).rjust(3), chr(pos) 
        else:
            print
            print "Unknown command"
            print "    q          -> quit"
            print "    set C C    -> set Ciphertext to Cleartext"
            print "    setSpace C -> treat Ciphertext as Space"
            print "    m          -> show messages"
            print "    d          -> show dictionary"
            print "    f1         -> show letter frequencies"
            print "    f2         -> show digram frequencies"
            print "    f3         -> show trigram frequencies"
            print "    s          -> show all"
            print "    a          -> toggleAutoCol"
            print "    try Caesar -> ..."
            print "    try Atbash -> ..."
            print "    TODO ascii"
            print "    TODO tables"
            print "    TODO "
            print "    TODO loadDic"
            print "    TODO saveDic"
            print "    TODO loadMsg"
            print "    TODO saveMsg"
            print "    TODO refactor classes"
            print "    TODO double map"            
            print "    TODO "
            print
        self.lastCommand = command
