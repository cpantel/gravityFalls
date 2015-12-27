import unittest
from SubstitutionCipher import *

class TestAny(unittest.TestCase):
  def test_decrypt(self):
      sa = SubstitutionCipher()
      sa.setCode('A','B')
      
      self.assertEqual('B',sa.decrypt('A'))

if __name__ == '__main__':
    unittest.main()
