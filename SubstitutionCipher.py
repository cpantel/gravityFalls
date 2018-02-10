from Statistical import *
from Helper import *

class SubstitutionCipher(object):
  def __init__(self):
    self.code = {}
    self.stats = Statistical()

  def load(self, ciphertext):
    self.ciphertext = ciphertext
    for c in self.ciphertext:
      self.code[c] = "?"

  def showCodes(self):
    result = ''      
    for c in self.code:
      if self.code[c] != '':
        result += "%s %s\n" % ( c, self.code[c])
    return result

  def setCode(self, cipher, clear):
    if clear == '':
      clear = '#'
    self.code[cipher] = clear;

  def decrypt(self,ciphertext):
    result = ''
    lowerLimit = Helper.lowerLimit
    upperLimit = Helper.upperLimit
    for char in ciphertext:
      if Helper.inRange(char):
        if self.code[char] != '':
          result += self.code[char]
        else:
          result += '#'
      else:
        result += char               
    return result

  def accept(self, command, ciphertext):
    if command[0:1] == 'd':
      return (True, False, self.showCodes())
    elif command[0:4] == 'set ':
      self.setCode(command[4:5], command[6:7])
      return (True, False, '')
    elif command == 'try Substitution':
      return (True, False, self.decrypt(ciphertext))
    else:
      return self.stats.accept(command, ciphertext, self.code)

