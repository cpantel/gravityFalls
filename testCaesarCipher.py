import unittest
from CaesarCipher import *

class TestCaesarCipher(unittest.TestCase):
  def test_decrypt(self):
      sa = CaesarCipher()
      
      self.assertEqual("xyz",sa.decrypt("abc",3))



if __name__ == '__main__':
    unittest.main()