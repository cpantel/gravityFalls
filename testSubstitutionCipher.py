import unittest
from SubstitutionCipher import *

class TestAny(unittest.TestCase):
  def test_decrypt(self):
      sa = SubstitutionCipher()
      sa.setCode('A','B')
      
      self.assertEqual('B',sa.decrypt('A'))

  def test_lower_decrypt(self):
      sa = SubstitutionCipher()
      sa.setCode('a','b')
      
      self.assertEqual('B',sa.decrypt('A'))


  def test_accept(self):
      sa = SubstitutionCipher()
      self.assertEqual((False,False,''), sa.accept('command','arguments'))
      
if __name__ == '__main__':
    unittest.main()
