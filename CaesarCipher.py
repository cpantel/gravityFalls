import sys

class CaesarCipher(object):
  
  def decrypt(self,ciphertext,offset):
     lowerLimit = ord("A")
     upperLimit = ord("Z")
     fix = 1 + ord("Z") - ord("A")
     result = ''
     for char in ciphertext:
        if ord(char) < lowerLimit or ord(char) > upperLimit:
          result += char
        else:
          fixed = ord(char)- offset
          if fixed < lowerLimit:
            fixed = fixed + fix 
          result += chr(fixed)
     return result     
     
  
  def tryAll(self,ciphertext):
    sys.stdout.write("    ")   
    sys.stdout.write(ciphertext)
    sys.stdout.write("\n")
    for offset in range(1,26):
      sys.stdout.write( repr(offset).rjust(3))
      sys.stdout.write(" ")
      sys.stdout.write(self.decrypt(ciphertext,offset))
      sys.stdout.write("\n")