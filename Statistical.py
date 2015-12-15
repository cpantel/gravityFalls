# -*- coding: utf-8 -*-

import sys
import os
import re
from Helper import *
from Printer import *

'''
pending refactor

instead of code receive a SubstitutionCipher and ask it for the translation

'''
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
          
  def freqW(self,ciphertext):
    self.statsW = {}
    for w in re.compile("[^A-Z]").split(ciphertext):
      if w:
        if w in self.statsW:
          self.statsW[w] += 1
        else:
          self.statsW[w] = 1
 
  def freqD(self, ciphertext):
    self.statsD = {}
    for match in re.compile(r"(.)\1{1}").finditer(ciphertext):
      d = match.group(0)
      if d in self.statsD:
        self.statsD[d] += 1
      else:
        self.statsD[d] = 1

  def freqFW(self,ciphertext):
    self.freqW(ciphertext)   
    self.statsFW = {}

    for w in self.statsW:
      c = w[0]
      if c in self.statsFW:
        self.statsFW[c] += self.statsW[w]
      else:
        self.statsFW[c] = self.statsW[w]

  # I suspect that this method belongs to its own class
  def pattern(self, ciphertext):
    current = 'a'
    pattern = ''
    table = {}

    for c in ciphertext:
      if c in table:
        pattern += table[c]
      else:
        table[c] = current
        pattern += current
        current = chr(ord(current) + 1)
    return pattern
  
  # No doubt...
  def buildPatterns(self, nameIn ):
    with open(nameIn,'r') as f:
      for word in f:
        word = word.strip()
        print "%32s : %32s" % ( self.pattern(word), word)
  
  def showPatterns(self,ciphertext,code):
    result = ''
    self.freqW(ciphertext)
    for word in self.statsW:
      pattern = self.pattern(word)
# refactor translation
      translated = ''
      for c in word:
        translated += code[c]      
      result += "%32s:%3d -> %20s (%s)\n" % (word, self.statsW[word], pattern, translated)      
    return result 

  def showFrequencies1(self,code):
    result = ''
    for c in sorted(self.stats1, key=self.stats1.get, reverse = True):
      # refactor translation
      result += "%s:%3d -> %s\n" % (c, self.stats1[c], code[c])
    return result

  def showFrequencies2(self,code):
    result = ''
    for c in sorted(self.stats2, key=self.stats2.get, reverse = True):
      # refactor translation
      result += "%s:%3d -> %s\n" % (c, self.stats2[c],code[c[0:1]] + code[c[1:2]])
    return result

  def showFrequencies3(self,code):
    result = ''
    for c in sorted(self.stats3, key=self.stats3.get, reverse = True):
      # refactor translation
      result += "%s:%3d -> %s\n" % (c, self.stats3[c],code[c[0:1]] + code[c[1:2]] + code[c[2:3]])
    return result

  def showFrequenciesW(self,code):
    result = ''
    for w in sorted(self.statsW, key=self.statsW.get, reverse = True):
      # refactor translation
      translated = ''
      for c in w:
        #try:
          translated += code[c]
        #except KeyError:
          #translated += 'Z'       
      result += "%30s:%3d -> %s\n" % (w,self.statsW[w], translated)
    return result

  def showFrequenciesFW(self,code):
    result = ''
    for c in sorted(self.statsFW, key=self.statsFW.get, reverse = True):
      # refactor translation
      result += "%s:%3d -> %s\n" % (c, self.statsFW[c],code[c])
    return result

  def showFrequenciesD(self,code):
    result = ''
    for c in sorted(self.statsD, key=self.statsD.get, reverse = True):
      # refactor translation
      result += "%s:%3d -> %s\n" % (c, self.statsD[c],code[c[0:1]] + code[c[1:2]])
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
    elif command[0:2] == 'fw':
      self.freqW(ciphertext)
      return (True, False, self.showFrequenciesW(code))
    elif command[0:2] == 'fd':
      self.freqD(ciphertext)
      return (True, False, self.showFrequenciesD(code))
    elif command[0:3] == 'ffw':
      self.freqFW(ciphertext)
      return (True, False, self.showFrequenciesFW(code))
    elif command[0:8] == 'pattern ':
      return (True, False, self.pattern(command[8:]))
    elif command[0:8] == 'patterns':
      return (True, False, self.showPatterns(ciphertext,code))
    return (False,False,'')
