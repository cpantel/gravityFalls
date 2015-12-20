import unittest
from SubstitutionCipher import *

class TestAny(unittest.TestCase):
  def test_upper(self):
      sa = SubstitutionCipher()

  def test_load(self):
     sa = SubstitutionCipher()
     sa.load         ("zhofrph wr judylwb idoov")
     self.assertEqual("????????????????????????",sa.cleartext)

if __name__ == '__main__':
    unittest.main()
