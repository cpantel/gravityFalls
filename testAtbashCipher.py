import unittest
from AtbashCipher import *

class TestAtbashCipher(unittest.TestCase):
  def test_decrypt(self):
      sa = AtbashCipher()
      
      self.assertEqual("zyxwvutsrqponmlkjihgfedcba",sa.decrypt("abcdefghijklmnopqrstuvwxyz"))

  def test_decryptA(self):
      sa = AtbashCipher()
      
      self.assertEqual("z",sa.decrypt("a"))

  def test_decryptZ(self):
      sa = AtbashCipher()
      
      self.assertEqual("a",sa.decrypt("z"))



if __name__ == '__main__':
    unittest.main()