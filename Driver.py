import sys
import os
from CaesarCipher import *
from AtbashCipher import *
from SubstitutionCipher import *
from Printer import *

class Driver(object):
    def __init__(self):
         self.exit = False
         self.printer = Printer()
         self.caesarCipher =  CaesarCipher()           
         self.atbashCipher =  AtbashCipher()
         self.substitutionCipher =  SubstitutionCipher()
         self.printer.setCols()


    def load(self, ciphertext):
        self.ciphertext = ciphertext
        self.cleartext = '?' * len(self.ciphertext)
        self.substitutionCipher.load(self.ciphertext)

  
    #def showMessages(self):
        #idx=0
        #while idx * self.colWidth < len(self.ciphertext): 
            #sys.stdout.write( self.ciphertext[idx * self.colWidth :(idx * self.colWidth) + self.colWidth])
            #times = len(self.ciphertext) / ( idx + 1 )
            #if times < self.colWidth:
                #spaces = ' ' * ( 4 + self.colWidth - (len(self.ciphertext) - idx * self.colWidth ) )
            #else:
                #spaces = ' ' * 4
                     
            #sys.stdout.write( spaces )
            #sys.stdout.write( self.cleartext[idx * self.colWidth :(idx * self.colWidth)  + self.colWidth])
            #print
            #idx = idx + 1

    #def show(self):
        #self.showMessages()
        #self.showDic()
        #self.showFrequencies()

 

    def accept(self):
        command = raw_input('?: ')             
        ### self.setCols()

        if command == 'q' or command == 'quit':
            return False
        #elif command == '' or command[0:1] == 'm':
            #self.showMessages()
        #elif command[0:1] == 'c': 
            #self.setCols()  # command[1:5]
        #elif command == 'a' or command == 'autoCol':
            #self.stats.toggleAutoCol()
        elif command == 's' or command == 'show':
            result = (True,True,self.ciphertext);
        else:
           handlers = { self.atbashCipher, self.substitutionCipher,  self.caesarCipher, Helper }
           for handler in handlers:
              result = handler.accept(command, self.ciphertext)
              (handled, error, result) = result
              if (handled or error):
                 break
              
        if (not handled):
           self.printHelp()
        else:
           print result
   
        return True

    def printHelp(self):
            print
            print "Unknown command"
            print "    q                -> quit"
            print "    set C C          -> set Ciphertext to Cleartext"
            print "    m                -> show messages"
            print "    c                -> show code"
            print "    f1               -> show letter frequencies"
            print "    f2               -> show digram frequencies"
            print "    f3               -> show trigram frequencies"
            print "    s                -> show all"
            print "    a                -> toggleAutoCol"
            print "    try Caesar       -> ..."
            print "    try Atbash       -> ..."
            print "    try Substitution -> ..."
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
