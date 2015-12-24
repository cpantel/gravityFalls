import unittest
from Helper import *

class TestAny(unittest.TestCase):
  def test_charInRangeOK(self):
     self.assertTrue(Helper.inRange('A'))
     self.assertTrue(Helper.inRange('Z'))               

  def test_notCharInRange(self):
     self.assertFalse(Helper.inRange('1'))
     self.assertFalse(Helper.inRange('a'))
     self.assertFalse(Helper.inRange('z'))

  def test_stringInRangeOK(self):
     self.assertTrue(Helper.inRange('AZ'))
     self.assertTrue(Helper.inRange('ZA'))     

  def test_notStringInRangeOK(self):
     self.assertFalse(Helper.inRange('A Z'))
     self.assertFalse(Helper.inRange('ZAa'))     


if __name__ == '__main__':
    unittest.main()