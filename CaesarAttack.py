import sys

class CaesarAttack(object):
  
  def decrypt(self,ciphertext,offset):
     lowerLimit = ord("a")
     upperLimit = ord("z")
     fix = 1 + ord("z") - ord("a")
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