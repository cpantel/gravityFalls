from Statistical import *
from Helper import *

class SubstitutionCipher(object):
  def __init__(self):
    self.dictionary = {}
    self.stats = Statistical()

  def load(self, ciphertext):
    self.ciphertext = ciphertext
    for c in self.ciphertext:
      self.dictionary[c] = "?"

  def showDic(self):
    result = ''      
    for c in self.dictionary:
      if self.dictionary[c] != '':
        result += "%s %s\n" % ( c, self.dictionary[c])
    return result

  def setDic(self, cipher, clear):
    if clear == '':
      clear = '#'
    self.dictionary[cipher] = clear;

  def decrypt(self,ciphertext):
    result = ''
    lowerLimit = Helper.lowerLimit
    upperLimit = Helper.upperLimit
    for char in ciphertext:
      if Helper.inRange(char):
        if self.dictionary[char] != '':
          result += self.dictionary[char]
        else:
          result += '#'
      else:
        result += char               
    return result

  def accept(self, command, ciphertext):
    if command[0:1] == 'd':
      return (True, False, self.showDic())
    elif command[0:4] == 'set ':
      self.setDic(command[4:5], command[6:7])
      return (True, False, '')
    elif command == 'try Substitution':
      return (True, False, self.decrypt(ciphertext))
    else:
      return self.stats.accept(command, ciphertext, self.dictionary)

