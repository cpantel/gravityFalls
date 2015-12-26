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
           result +=  "%(posoffset)3d %(chrposoffset)s %(pos)3d %(chrpos)s\n" % \
               {'posoffset' :pos + offset, 'chrposoffset': chr(pos+offset), 'pos': pos, 'chrpos' : chr(pos)}
        return result
     
    @staticmethod
    def accept(command, ciphertext):
       if command == 'ascii':
          return (True, False, Helper.asciiTable())
       return (False, False, '')
