class AtbashAttack(object):
  
  def run(self,ciphertext):
    sys.stdout.write("    ")   
    sys.stdout.write(ciphertext)
    sys.stdout.write("\n")
    
    lowerLimit = ord("a")
    upperLimit = ord("z")

    fix = 1 + ord("z") - ord("a")

    for char in ciphertext:
      if ord(char) < lowerLimit or ord(char) > upperLimit:
        sys.stdout.write(char)
      else:
        fixed = ord(char)- offset
        if fixed < lowerLimit:
          fixed = fixed + fix 
        sys.stdout.write(chr(fixed))
    sys.stdout.write("\n")