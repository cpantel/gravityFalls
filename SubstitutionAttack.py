import sys
import os
from Statistical import *
from CaesarAttack import *
from AtbashAttack import *

class SubstitutionAttack(object):
    def __init__(self):
         self.exit = False
         self.dic = {}
         self.buffer = ""
         self.setCols()
         self.stats = Statistical()

    def setCols(self):
#         tty = subprocess.Popen('stty size', 'r')

         tty = os.popen('stty size', 'r')
         rows, columns = tty.read().split()
         self.colWidth = (int(columns) - 4) / 2

    def load(self, ciphertext):
        self.ciphertext = ciphertext
        self.cleartext = '?' * len(self.ciphertext)

        for c in self.ciphertext:
            self.dic[c] = "?"
        self.calculateFreq()

    def calculateFreq(self):
        self.stats.freq1(self.ciphertext)
        self.stats.freq2(self.ciphertext)
        self.stats.freq3(self.ciphertext)
     
    def showMessages(self):
        idx=0
        while idx * self.colWidth < len(self.ciphertext): 
            sys.stdout.write( self.ciphertext[idx * self.colWidth :(idx * self.colWidth) + self.colWidth])
            times = len(self.ciphertext) / ( idx + 1 )
            if times < self.colWidth:
                spaces = ' ' * ( 4 + self.colWidth - (len(self.ciphertext) - idx * self.colWidth ) )
            else:
                spaces = ' ' * 4
                     
            sys.stdout.write( spaces )
            sys.stdout.write( self.cleartext[idx * self.colWidth :(idx * self.colWidth)  + self.colWidth])
            print
            idx = idx + 1

    def showDic(self):
        for c in self.dic:
            if self.dic[c] != "?":
                print "%s %s" % ( c, self.dic[c])

    def outputLine(self,text):
        if len(self.buffer) + len(text) > (self.colWidth * 2 ) + 1:
            self.flush()
        else:
            self.buffer += text + " "

    def flush(self):
        if len(self.buffer) != 0:
            print(self.buffer)
            self.buffer = ""

    def showFrequencies1(self):
        self.stats.showFrequencies1(self.dic)

    def showFrequencies2(self):
        self.stats.showFrequencies2(self.dic)

    def showFrequencies3(self):
        self.stats.showFrequencies3(self.dic)

    def showFrequencies(self):
        self.showFrequencies1()
        self.showFrequencies2()
        self.showFrequencies3()

    def show(self):
        self.showMessages()
        self.showDic()
        self.showFrequencies()

    def accept(self):
        command = raw_input('?: ')             
        self.setCols()
        if command == 'q' or command == 'quit':
            self.exit = True
        elif command == '' or command[0:1] == 'm':
            self.showMessages()
        elif command[0:1] == 'd':
            self.showDic()
        elif command[0:2] == 'f1':
            self.showFrequencies1()
        elif command[0:2] == 'f2':
            self.showFrequencies2()
        elif command[0:2] == 'f3':
            self.showFrequencies3()
        elif command[0:1] == 'f':
            self.showFrequencies()
        elif command[0:1] == 'c': 
            self.setCols()  # command[1:5]
        elif command == 'a' or command == 'autoCol':
            self.stats.toggleAutoCol()
        elif command[0:4] == 'set ':
            if command[6:7]:
                self.dic[command[4:5]] = command[6:7]
            else:
                self.dic[command[4:5]] = '?'
            attacker.decrypt()
        elif command[0:9] == 'setSpace ':
            if command[9:10]:
                self.dic[command[9:10]] = " "
                self.stats.spacing = command[9:10]
            else:
                self.dic[command[9:10]] = '?'
                self.stats.spacing = False
            self.calculateFreq()
            attacker.decrypt()
        elif command == 's' or command == 'show':
            self.show()
        elif command == 'try Caesar':
            caesarAttack =  CaesarAttack()
            caesarAttack.run(self.ciphertext)
        elif command == 'try Atbash':
            atbashAttack =  AtbashAttack()
            atbashAttack.run(self.ciphertext)
        elif command == 'ascii':
           lowerLimit = ord("a")
           upperLimit = ord("z")        
           offset = - 32

           for pos in range(lowerLimit, upperLimit):
              print pos + offset, chr(pos + offset), repr(pos).rjust(3), chr(pos) 
        else:
            print
            print "Unknown command"
            print "    q          -> quit"
            print "    set C C    -> set Ciphertext to Cleartext"
            print "    setSpace C -> treat Ciphertext as Space"
            print "    m          -> show messages"
            print "    d          -> show dictionary"
            print "    f1         -> show letter frequencies"
            print "    f2         -> show digram frequencies"
            print "    f3         -> show trigram frequencies"
            print "    s          -> show all"
            print "    a          -> toggleAutoCol"
            print "    try Caesar -> ..."
            print "    try Atbash -> ..."
            print "    TODO loadDic"
            print "    TODO saveDic"
            print "    TODO loadMsg"
            print "    TODO saveMsg"
            print "    TODO refactor classes"
            print "    TODO double map"            
            print "    TODO "
            print
        self.lastCommand = command
    def decrypt(self):
        self.cleartext = ""
        for c in self.ciphertext:
            self.cleartext += self.dic[c]



'''
cleartext=

  string[x:y]

    stringVar.count('x') - counts the number of occurrences of 'x' in stringVar
    stringVar.find('x') - returns the position of character 'x'
    stringVar.lower() - returns the stringVar in lowercase (this is temporary)
    stringVar.upper() - returns the stringVar in uppercase (this is temporary)
    stringVar.replace('a', 'b') - replaces all occurrences of a with b in the string
    stringVar.strip() - removes leading/trailing white space from string

  list[e1,e2,e3]

    .append(value) - appends element to end of the list
    .count('x') - counts the number of occurrences of 'x' in the list
    .index('x') - returns the index of 'x' in the list
    .insert('y','x') - inserts 'x' at location 'y'
    .pop() - returns last element then removes it from the list
    .remove('x') - finds and removes first 'x' from list
    .reverse() - reverses the elements in the list
    .sort() - sorts the list alphabetically in ascending order, or numerical in ascending order

  tuple(e1,e2,e3)

  dictionary {'key1': value, 'key2':value}

if ...:
elif ...:
else:

def function():

for idx in :
 ....

while ...:
'''
