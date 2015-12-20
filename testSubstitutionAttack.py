import unittest
from SubstitutionAttack import *

class TestAny(unittest.TestCase):
  def test_upper(self):
      sa = SubstitutionAttack()

  def test_load(self):
     sa = SubstitutionAttack()
     sa.load         ("zhofrph wr judylwb idoov")
     self.assertEqual("????????????????????????",sa.cleartext)

if __name__ == '__main__':
    unittest.main()
