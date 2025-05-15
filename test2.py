

import unittest
from second_task import PDA_simulate

class TestPDASimulator(unittest.TestCase):

    def test_empty_string(self):
        """ Test empty string """
        self.assertTrue(PDA_simulate(""))

    def test_single_pair(self):
        """ Test 'ab' """
        self.assertTrue(PDA_simulate("ab"))

    def test_multiple_pairs(self):
        """ Test 'aabb' and 'aaabbb' """
        self.assertTrue(PDA_simulate("aabb"))
        self.assertTrue(PDA_simulate("aaabbb"))

    def test_unequal_a_b(self):
        """ Test strings with unequal 'a' and 'b' """
        self.assertFalse(PDA_simulate("aab"))
        self.assertFalse(PDA_simulate("abb"))
        self.assertTrue(PDA_simulate("aaaaaabbbbbb"))

    def test_only_a(self):
        """ Test strings with only 'a' characters """
        self.assertFalse(PDA_simulate("aaa"))

    def test_only_b(self):
        """ Test strings with only 'b' characters """
        self.assertFalse(PDA_simulate("bbb"))

if __name__ == "__main__":
    unittest.main()
