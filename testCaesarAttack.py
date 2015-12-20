import unittest
from CaesarAttack import *

class TestCaesarAttack(unittest.TestCase):
  def test_freq1(self):
      sa = CaesarAttack()
      
      self.assertEqual("xyz",sa.decrypt("abc",3))



if __name__ == '__main__':
    unittest.main()