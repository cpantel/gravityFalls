import itertools

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
    result = []
    offset = 32
    for pos in range(Helper.lowerLimit, Helper.upperLimit):
      result.append(  "%3d %s %3d %s" % (pos + offset, chr(pos+offset), pos,chr(pos)))
    return result
  
  @staticmethod
  def englishCorpusF1():
    return  ['E','T','A','O','I','N','S','R','H','L','D','C','U','M','F','G','P','W','Y','B','V','K','J','X','Z','Q']
  
  @staticmethod
  def englishCorpusF2():
    return ['TH','HE','IN','ER','AN','RE','ES','ON','ST','NT','EN','AT','ED','ND','TO','OR','EA','TI','AR','TE','NG','AL','IT','AS','IS','HA','ET','SE','OU','OF']
  
  @staticmethod
  def englishCorpusF3():
    return ['THE','AND','ING','ENT','ION','HER','FOR','THA','NTH','INT','ERE','TIO','TER','EST','ERS','ATI','HAT','ATE','ALL','HES','VER','HIS','ETH','OFT','ITH','FTH','STH','OTH','RES','ONT']
  
  @staticmethod
  def englishCorpusFW():
    return ['THE','OF','AND','TO','A','IN','IS','FOR','THAT','WAS','ON','WITH','HE','IT','AS','AT','HIS','BY','BE','ARE','FROM','THIS','I','BUT','HAVE','AN','HAS','NOT','THEY','OR']
  
  @staticmethod
  def englishCorpusFFW():
    return ['T','A','S','H','W','I','O','B','M','F','C','L','D','P','N','E','G','R','Y','U','V','J','K','Q','Z','X']
  
  @staticmethod
  def englishCorpusFD():
    return ['LL','SS','EE','OO','TT','FF','RR','NN','PP','CC','MM','GG','DD','AA','BB']
  
  @staticmethod
  def showEnglishCorpus():
    sformat = "%11s | %6s | %6s | %6s | %6s | %6s | %6s\n"
    result = sformat % ("ascii", "f1", "f2", "f3", "ffw","fw", "fd")
    for at, f1, f2, f3,ffw,fw, fd in itertools.izip_longest( \
        Helper.asciiTable(), Helper.englishCorpusF1(), Helper.englishCorpusF2(), Helper.englishCorpusF3(), Helper.englishCorpusFFW(), Helper.englishCorpusFW(), Helper.englishCorpusFD() \
    ):
      if f1 == None:
        f1 = ''
      if f2 == None:
        f2 = ''
      if f3 == None:
        f3 = ''
      if ffw == None:
        ffw = ''
      if fw == None:
        fw = ''
      if at == None:
        at = ''
      if fd == None:
        fd = ''
      result += sformat % (at,f1, f2, f3, ffw, fw, fd)
    return result
     
     
  @staticmethod
  def accept(command, ciphertext):
    if command == 'english corpus':
      return (True, False, Helper.showEnglishCorpus())
    return (False, False, '')
