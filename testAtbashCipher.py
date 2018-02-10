import unittest
from AtbashCipher import *

class TestAtbashCipher(unittest.TestCase):
  def test_decrypt(self):
      sa = AtbashCipher()
      
      self.assertEqual("ZYXWVUTSRQPONMLKJIHGFEDCBA",sa.decrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

  def test_decryptA(self):
      sa = AtbashCipher()
      
      self.assertEqual("Z",sa.decrypt("A"))

  def test_decryptZ(self):
      sa = AtbashCipher()
      
      self.assertEqual("A",sa.decrypt("Z"))

  def test_accept(self):
      sa = AtbashCipher()
      self.assertEqual((False,False,''), sa.accept('command','arguments'))

if __name__ == '__main__':
    unittest.main()