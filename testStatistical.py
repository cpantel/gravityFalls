import unittest
from Statistical import *

class TestAny(unittest.TestCase):
  def test_freq1(self):
      sa = Statistical()
      sa.freq1("abbcccdddd")
      self.assertEqual({'a':1,'b':2,'c':3,'d':4},sa.stats1)

  def test_freq2(self):
      sa = Statistical()
      sa.freq2("abbcccdddd")
      self.assertEqual({'ab':1,'bb':1,'bc':1,'cc':2,'cd':1,'dd':3},sa.stats2)

  def test_freq3(self):
      sa = Statistical()
      sa.freq3("abbcccdddd")
      self.assertEqual({'abb':1,'bbc':1,'bcc':1,'ccc':1,'ccd':1,'cdd':1,'ddd':2},sa.stats3)

  def test_spaced_freq1(self):
      sa = Statistical()
      sa.spacing = ' '
      sa.freq1("a bb ccc dddd")
      self.assertEqual({'a':1,'b':2,'c':3,'d':4},sa.stats1)

  def test_spaced_freq2(self):
      sa = Statistical()
      sa.spacing = ' '      
      sa.freq2("a bb ccc dddd")
      self.assertEqual({'bb':1,'cc':2,'dd':3},sa.stats2)

  def test_spaced_freq3(self):
      sa = Statistical()
      sa.spacing = ' '      
      sa.freq3("a bb ccc dddd")
      self.assertEqual({'ccc':1,'ddd':2},sa.stats3)

if __name__ == '__main__':
    unittest.main()