import sys
import os

class Printer(object):
    def __init__(self):
         self.autoCol = False
         self.buffer = ""
         tty = os.popen('stty size', 'r')
         rows, columns = tty.read().split()
         self.colWidth = (int(columns) - 4) / 2
    def outputLine(self,text):
      if self.autoCol:
        if len(self.buffer) + len(text) > (self.colWidth * 2 ) + 1:
            self.flush()
        else:
            self.buffer += text + " "
      else:
        print text

    def setCols(self):      # driver
#         tty = subprocess.Popen('stty size', 'r')

         tty = os.popen('stty size', 'r')
         rows, columns = tty.read().split()
         self.colWidth = (int(columns) - 4) / 2


    def toggleAutoCol(self):
      self.autoCol = not self.autoCol

    def flush(self):
        if len(self.buffer) != 0:
            print(self.buffer)
            self.buffer=""
                    