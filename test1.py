import unittest
from first_task import DFA_divided

class TestDFA(unittest.TestCase):
    def test_accepted_cases(self):
        self.assertEqual(DFA_divided("1101"), "Accepted")    
        self.assertEqual(DFA_divided("1001"), "Rejected")    
        self.assertEqual(DFA_divided("110010010101"), "Accepted")  

    def test_rejected_cases(self):
        self.assertEqual(DFA_divided("1011"), "Accepted")     
        self.assertEqual(DFA_divided("0001"), "Rejected")     
        self.assertEqual(DFA_divided("11000000000000001111"), "Accepted") 
        self.assertEqual(DFA_divided("1100"), "Rejected")    

    def test_invalid_input(self):
        self.assertEqual(DFA_divided("12000"), "Invalid input")
        self.assertEqual(DFA_divided("10a01"), "Invalid input")

if __name__ == "__main__":
    unittest.main()
