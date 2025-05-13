import unittest
from first_task import DFA_divided

class TestDFA(unittest.TestCase):
    def test_accepted_cases(self):
        self.assertEqual(DFA_divided("1101"), "Accepted")     # 3 ones
        self.assertEqual(DFA_divided("1001"), "Rejected")     # 3 ones
        self.assertEqual(DFA_divided("110010010101"), "Accepted")  # 6 ones

    def test_rejected_cases(self):
        self.assertEqual(DFA_divided("1011"), "Accepted")     # 4 ones
        self.assertEqual(DFA_divided("0001"), "Rejected")     # 1 one
        self.assertEqual(DFA_divided("11000000000000001111"), "Accepted")  # 7 ones
        self.assertEqual(DFA_divided("1100"), "Rejected")     # 2 ones

    def test_invalid_input(self):
        self.assertEqual(DFA_divided("12000"), "Invalid input")
        self.assertEqual(DFA_divided("10a01"), "Invalid input")

if __name__ == "__main__":
    unittest.main()
