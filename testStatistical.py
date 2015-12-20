import unittest
from Statistical import *

class TestAny(unittest.TestCase):
  def test_freq1(self):
      sa = Statistical()
      sa.freq1("ABBCCCDDDD")
      self.assertEqual({'A':1,'B':2,'C':3,'D':4},sa.stats1)

  def test_freq2(self):
      sa = Statistical()
      sa.freq2("ABBCCCDDDD")
      self.assertEqual({'AB':1,'BB':1,'BC':1,'CC':2,'CD':1,'DD':3},sa.stats2)

  def test_freq3(self):
      sa = Statistical()
      sa.freq3("ABBCCCDDDD")
      self.assertEqual({'ABB':1,'BBC':1,'BCC':1,'CCC':1,'CCD':1,'CDD':1,'DDD':2},sa.stats3)

  def test_spaced_freq1(self):
      sa = Statistical()
      sa.spacing = ' '
      sa.freq1("A BB CCC DDDD")
      self.assertEqual({'A':1,'B':2,'C':3,'D':4},sa.stats1)

  def test_spaced_freq2(self):
      sa = Statistical()
      sa.spacing = ' '      
      sa.freq2("A BB CCC DDDD")
      self.assertEqual({'BB':1,'CC':2,'DD':3},sa.stats2)

  def test_spaced_freq3(self):
      sa = Statistical()
      sa.spacing = ' '      
      sa.freq3("A BB CCC DDDD")
      self.assertEqual({'CCC':1,'DDD':2},sa.stats3)

if __name__ == '__main__':
    unittest.main()