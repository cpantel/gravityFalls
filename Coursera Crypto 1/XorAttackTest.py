#!/usr/bin/python
import unittest
import XorAttack

class TestXorAttack(unittest.TestCase):
    def setUp(self):
        self.attacker = XorAttack.XorAttack()

    def test_fixCols(self):
        self.assertEqual(0,self.attacker.fixCols())

if __name__ == '__main__':
    unittest.main()
