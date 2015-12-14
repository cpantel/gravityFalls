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
  def test_showTables(self):
     output = Helper.showEnglishCorpus()
     print "\n" +  output
     lines=output.split("\n");
     self.assertEqual(lines[0], "      ascii |     f1 |     f2 |     f3 |    ffw |     fw |     fd" )
     self.assertEqual(lines[1], " 97 a  65 A |      E |     TH |    THE |      T |    THE |     LL" )
     self.assertEqual(lines[30],"            |        |     OF |    ONT |        |     OR |       " )
     
if __name__ == '__main__':
    unittest.main()