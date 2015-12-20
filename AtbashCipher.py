import sys

class AtbashCipher(object):
  
  def decrypt(self,ciphertext):
    lowerLimit = ord("a")
    upperLimit = ord("z")
    distance = upperLimit - lowerLimit
    result = ''

    for char in ciphertext:
      pos = ord(char)
      if pos < lowerLimit or pos > upperLimit:
        result += char
      else:
        result += chr(lowerLimit + upperLimit - pos)
    return result
  
  def run(self,ciphertext):
    sys.stdout.write("    ")   
    sys.stdout.write(ciphertext)
    sys.stdout.write("\n")
    sys.stdout.write("    ")     
    sys.stdout.write(self.decrypt(ciphertext))
    sys.stdout.write("\n")