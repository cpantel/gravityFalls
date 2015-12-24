import sys
from Helper import *

class CaesarCipher(object):
  
  def decrypt(self,ciphertext,offset):
     lowerLimit = Helper.lowerLimit
     upperLimit = Helper.upperLimit
     fix = 1 + upperLimit - lowerLimit
     result = ''
     for char in ciphertext:
        if ord(char) < lowerLimit or ord(char) > upperLimit:
          result += char
        else:
          fixed = ord(char)- offset
          if fixed < lowerLimit:
            fixed = fixed + fix 
          result += chr(fixed)
     return result     

  def accept(self, command):
        if command == 'try Caesar':
            self.tryIt(self.ciphertext)            
        else:
           return False
        return True     
  
  def tryIt(self,ciphertext):
    sys.stdout.write("    ")   
    sys.stdout.write(ciphertext)
    sys.stdout.write("\n")
    for offset in range(1,26):
      sys.stdout.write( repr(offset).rjust(3))
      sys.stdout.write(" ")
      sys.stdout.write(self.decrypt(ciphertext,offset))
      sys.stdout.write("\n")