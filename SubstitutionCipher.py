# -*- coding: utf-8 -*-
from Statistical import *
from Helper import *

class SubstitutionCipher(object):
  def __init__(self):
    self.code = {}
    self.stats = Statistical()

  def showCodes(self):
    result = ''      
    for c in self.code:
      if self.code[c] != '':
        result += "%s %s\n" % ( c, self.code[c])
    return result

  def setCode(self, cipher, clear):
    if clear == '':
      clear = '·'
    self.code[cipher] = clear;

  def updateCodes(self, ciphertext):
    for c in ciphertext:
      if Helper.inRange(c):
        try:
          self.code[c]
        except KeyError:
          self.code[c] = '·'

  def decrypt(self,ciphertext):
    self.updateCodes(ciphertext)
    result = ''
    lowerLimit = Helper.lowerLimit
    upperLimit = Helper.upperLimit
    for char in ciphertext:
      if Helper.inRange(char):
        result += self.code[char]
      else:
        result += char               
    return result

  def accept(self, command, ciphertext):
    if command == 'codes':
      return (True, False, self.showCodes())
    elif command[0:4] == 'set ':
      self.setCode(command[4:5], command[6:7])
      return (True, False, '')
    elif command == 'try Substitution':
      return (True, False, '    ' + self.decrypt(ciphertext))
    else:
      self.updateCodes(ciphertext)
      return self.stats.accept(command, ciphertext, self.code)

