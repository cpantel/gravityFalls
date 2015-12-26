from Statistical import *
from Helper import *

class SubstitutionCipher(object):
    def __init__(self):
         self.dic = {}
         self.stats = Statistical()

    def load(self, ciphertext):
        self.ciphertext = ciphertext
        for c in self.ciphertext:
            self.dic[c] = "?"

    def showDic(self):
        for c in self.dic:
            if self.dic[c] != '':
                print "%s %s" % ( c, self.dic[c])

    def setDic(self, cipher, clear):
       if clear == '':
          clear = '#'
       self.dic[cipher] = clear;

    def decrypt(self,ciphertext):
        result = ''
        lowerLimit = Helper.lowerLimit
        upperLimit = Helper.upperLimit
        for char in ciphertext:
            if Helper.inRange(char):
               if self.dic[char] != '':
                   result += self.dic[char]
               else:
                   result += '#'
            else:
               result += char               
        return result

    def tryIt(self,ciphertext):
       print self.decrypt

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




    def accept(self, command, ciphertext):
        if command[0:1] == 'd':
            self.showDic()
        elif command[0:4] == 'set ':
            self.setDic(command[4:5], command[6:7])    
        elif command == 'try Substitution':
            self.tryIt(self.ciphertext)
        elif command[0:2] == 'f1':
            self.showFrequencies1()
        elif command[0:2] == 'f2':
            self.showFrequencies2()
        elif command[0:2] == 'f3':
            self.showFrequencies3()
        elif command[0:1] == 'f':
            self.showFrequencies()            

        return (False,False,'')

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
