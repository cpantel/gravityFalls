#!/usr/bin/python
import sys
import os

class Statistical(object):
    def __init__(self):
         self.spacing = False
         self.autoCol = False
         self.buffer = ""
         tty = os.popen('stty size', 'r')
         rows, columns = tty.read().split()
         self.colWidth = (int(columns) - 4) / 2
         
    def freq1(self, text):         
        self.stats1 = {}
        for c in text:
          if self.spacing != False and c == self.spacing:
            pass
          else:
            if c in self.stats1:
                self.stats1[c] += 1
            else:
                self.stats1[c] = 1
                
    def freq2(self,text):
        self.stats2 = {}
        for idx in range(0,len(text) - 1):
          digram= text[idx:idx + 2]
          if self.spacing != False and self.spacing in digram:
            pass
          else:
            if digram in self.stats2:
                self.stats2[digram] += 1
            else:
                self.stats2[digram]=1
                
    def freq3(self,text):
        self.stats3 = {}
        for idx in range(0,len(text) - 2):
          trigram= text[idx:idx + 3]
          if self.spacing != False and self.spacing in trigram:
            pass
          else:
            if trigram in self.stats3:
                self.stats3[trigram] += 1
            else:
                self.stats3[trigram] = 1

    def showFrequencies1(self,dictionary):
        for c in sorted(self.stats1, key=self.stats1.get, reverse = True):
            self.outputLine(format("%s:%3d->%s" % (c, self.stats1[c],dictionary[c])))
        self.flush()

    def showFrequencies2(self,dictionary):
        for c in sorted(self.stats2, key=self.stats2.get, reverse = True):
            self.outputLine(format("%s:%2d->%s" % (c, self.stats2[c],dictionary[c[0:1]] + dictionary[c[1:2]])))
        self.flush()

    def showFrequencies3(self,dictionary):
        for c in sorted(self.stats3, key=self.stats3.get, reverse = True):
            self.outputLine(format("%s:%2d->%s" % (c, self.stats3[c],dictionary[c[0:1]] + dictionary[c[1:2]] + dictionary[c[2:3]])))
        self.flush()

    def outputLine(self,text):
      if self.autoCol:
        if len(self.buffer) + len(text) > (self.colWidth * 2 ) + 1:
            self.flush()
        else:
            self.buffer += text + " "
      else:
        print text

    def toggleAutoCol(self):
      self.autoCol = not self.autoCol

    def flush(self):
        if len(self.buffer) != 0:
            print(self.buffer)
            self.buffer=""
            
