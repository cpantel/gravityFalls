from Helper import *

class SubstitutionCipher(object):
    def __init__(self):
         self.dic = {}

    def load(self, ciphertext):   # driver
        self.ciphertext = ciphertext
        self.cleartext = '?' * len(self.ciphertext)

        for c in self.ciphertext: # replace with language function
            self.dic[c] = "?"
      #  self.calculateFreq()

    def showDic(self):
        for c in self.dic:
            if self.dic[c] != "?":
                print "%s %s" % ( c, self.dic[c])

    def decrypt(self):
        lowerLimit = Helper.lowerLimit
        upperLimit = Helper.upperLimit
        self.cleartext = ""
        for char in self.ciphertext:
            if ord(char) < lowerLimit or ord(char) > upperLimit: 
               self.cleartext += char
            else:
               self.cleartext += self.dic[char]



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
