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
  
  def tryIt(self,ciphertext):
    result = ''
    for offset in range(1,26):
      result += repr(offset).rjust(3) 
      result += " "
      result += self.decrypt(ciphertext,offset)
      result += "\n"
    return result


  def accept(self, command, ciphertext):
    if command == 'try caesar':
      return (True, False, self.tryIt(ciphertext))   
    return (False, False, '')
