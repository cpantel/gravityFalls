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
         self.ciphertext = ''

    def accept(self):
        command = raw_input('?: ')             
        command = command.strip()
        command = command.lower()
        if command == 'q' or command == 'quit':
            return False
        elif  command[0:1] == 'm':
          if command == 'm':
            (handled, error, result) = (True,False, '    ' + self.ciphertext)
          else:
            self.ciphertext = command[2:].upper()
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
            print "    set C C                -> set Code Ciphertext to  Cleartext (TODO: set CCCC CCCC)"
            print "    unset C                -> unset Code (like set C)           (TODO: unset CCCC")
            print "    m                      -> show messages"
            print "    codes                  -> show code"
            print "    f1                     -> show letter frequency"
            print "    f2                     -> show digram frequency"
            print "    f3                     -> show trigram frequency"
            print "    ffw                    -> show first char word frequency"
            print "    fw                     -> show word frequency"
            print "    fd                     -> show double char frequency"
            print "    pattern WORD           -> show WORD pattern"
            print "    patterns               -> show patterns"
            print "    try Caesar             -> decrypt with Caesar cipher"
            print "    try Atbash             -> decrypt with Atbash cipher"
            print "    try Substitution       -> decrypt with Substitution cipher"
            print "    english corpus         -> show known english corpus frequencies"
            print " (TODO) make corpus         -> use current message as corpus"
            print " (TODO) current corpus      -> show current corpus frequencies"
            print " (TODO) loadCodes FILENAME  -> load codes from file"
            print " (TODO) saveCodes FILENAME  -> save codes to file"
            print "    q                      -> quit"
            print
