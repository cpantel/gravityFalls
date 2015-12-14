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

    def accept(self):
        command = raw_input('?: ')             

        if command == 'q' or command == 'quit':
            return False
        elif  command[0:1] == 'm':
          if command == 'm':
            (handled, error, result) = (True,False, '    ' + self.ciphertext)
          else:
            self.ciphertext = command[2:]
            (handled, error, result) = (True, False, self.ciphertext)
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
