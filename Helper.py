class Helper(object):
    lowerLimit = ord("A")
    upperLimit = ord("Z")
   
    @staticmethod
    def inRange(char):
        pos = ord(char)
        return pos >= lowerLimit or pos <= upperLimit

    @staticmethod
    def asciiTable():
        offset = -32
        for pos in range(Helper.lowerLimit, Helper.upperLimit):
           print pos + offset, chr(pos + offset), repr(pos).rjust(3), chr(pos) 
