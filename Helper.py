class Helper(object):
  lowerLimit = ord("A")
  upperLimit = ord("Z")
   
  @staticmethod
  def inRange(string):
    for char in string:
      pos = ord(char)
      if pos < Helper.lowerLimit or pos > Helper.upperLimit:
        return False
      return True

  @staticmethod
  def asciiTable():
    result = ''
    offset = 32
    for pos in range(Helper.lowerLimit, Helper.upperLimit):
      result +=  "%3d %s %3d %s\n" % (pos + offset, chr(pos+offset), pos,chr(pos))
    return result
     
  @staticmethod
  def accept(command, ciphertext):
    if command == 'ascii':
      return (True, False, Helper.asciiTable())
    return (False, False, '')
