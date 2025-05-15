import unittest
from third_task import simulate_turing_machine

class TestTuringMachine(unittest.TestCase):

    def test_accepted_strings(self):
        accepted_cases = [
            "", "00", "11", "0101", "0011", "00110011"
        ]
        for case in accepted_cases:
            with self.subTest(case=case):
                self.assertTrue(simulate_turing_machine(case), f"Expected to accept: {case}")

    def test_rejected_strings(self):
        rejected_cases = [
            "0", "01", "001", "010", "0110", "000111", "011"
        ]
        for case in rejected_cases:
            with self.subTest(case=case):
                self.assertFalse(simulate_turing_machine(case), f"Expected to reject: {case}")

if __name__ == "__main__":
    unittest.main()
