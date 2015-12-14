import unittest
from Statistical import *

class TestStatistical(unittest.TestCase):
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
      sa.freq1("A BB CCC DDDD")
      self.assertEqual({'A':1,'B':2,'C':3,'D':4},sa.stats1)

  def test_spaced_freq2(self):
      sa = Statistical()
      sa.freq2("A BB CCC DDDD")
      self.assertEqual({'BB':1,'CC':2,'DD':3},sa.stats2)

  def test_spaced_freq3(self):
      sa = Statistical()
      sa.freq3("A BB CCC DDDD")
      self.assertEqual({'CCC':1,'DDD':2},sa.stats3)
      
  def test_freqW(self):
      sa = Statistical()
      sa.freqW("A")
      self.assertEqual({'A':1}, sa.statsW)
      
      sa.freqW("AAAA AAA AAA AA AA AA A A A A")
      self.assertEqual({'A':4,'AA':3,'AAA':2,'AAAA':1}, sa.statsW)

  def test_freqFW(self):
      sa = Statistical()
      sa.freqFW("A")
      self.assertEqual({'A':1}, sa.statsFW)
      
      sa.freqFW("ABCD ABC ABC AB AB AB A A A A B B B")
      self.assertEqual({'A':10,'B':3}, sa.statsFW)   

if __name__ == '__main__':
    unittest.main()