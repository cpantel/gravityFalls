import sys
import os
from Helper import *
from Printer import *

class Statistical(object):
        
  def freq1(self, ciphertext):         
    self.stats1 = {}
    for c in ciphertext:
      if Helper.inRange(c):
        if c in self.stats1:
          self.stats1[c] += 1
        else:
          self.stats1[c] = 1
                
  def freq2(self,ciphertext):
    self.stats2 = {}
    for idx in range(0,len(ciphertext) - 1):
      digram= ciphertext[idx:idx + 2]
      if  Helper.inRange(digram):
        if digram in self.stats2:
          self.stats2[digram] += 1
        else:
          self.stats2[digram]=1
              
  def freq3(self,ciphertext):
    self.stats3 = {}
    for idx in range(0,len(ciphertext) - 2):
      trigram= ciphertext[idx:idx + 3]
      if Helper.inRange(trigram):
        if trigram in self.stats3:
          self.stats3[trigram] += 1
        else:
          self.stats3[trigram] = 1

  def showFrequencies1(self,code):
    result = ''
    for c in sorted(self.stats1, key=self.stats1.get, reverse = True):
      result += "%s:%3d->%s" % (c, self.stats1[c],code[c])
    return result

  def showFrequencies2(self,code):
    result = ''
    for c in sorted(self.stats2, key=self.stats2.get, reverse = True):
      result += "%s:%2d->%s" % (c, self.stats2[c],code[c[0:1]] + code[c[1:2]])
    return result

  def showFrequencies3(self,code):
    result = ''
    for c in sorted(self.stats3, key=self.stats3.get, reverse = True):
      result += "%s:%2d->%s" % (c, self.stats3[c],code[c[0:1]] + code[c[1:2]] + code[c[2:3]])
    return result

  def accept(self, command,ciphertext, code):
    if command[0:2] == 'f1':
      self.freq1(ciphertext)
      return (True, False, self.showFrequencies1(code))
    elif command[0:2] == 'f2':
      self.freq2(ciphertext)
      return (True, False, self.showFrequencies2(code))
    elif command[0:2] == 'f3':
      self.freq3(ciphertext)
      return (True, False, self.showFrequencies3(code))
    return (False,False,'')
