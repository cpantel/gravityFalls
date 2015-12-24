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
        offset = -32
        for pos in range(Helper.lowerLimit, Helper.upperLimit):
           print pos + offset, chr(pos + offset), repr(pos).rjust(3), chr(pos) 

    @staticmethod
    def accept(command):
       if command == 'ascii':
          Helper.asciiTable()
       else:
          return False
       return True