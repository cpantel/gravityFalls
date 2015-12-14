import sys
from Helper import *

class AtbashCipher(object):
  
  def decrypt(self,ciphertext):
    lowerLimit = Helper.lowerLimit
    upperLimit = Helper.upperLimit
    distance = upperLimit - lowerLimit
    result = ''

    for char in ciphertext:
      pos = ord(char)
      if pos < lowerLimit or pos > upperLimit:
        result += char
      else:
        result += chr(lowerLimit + upperLimit - pos)
    return result

  def accept(self, command, ciphertext):
    if command == 'try Atbash':
      return (True, False, '    ' + self.decrypt(ciphertext))
    return (False, False, '')
    