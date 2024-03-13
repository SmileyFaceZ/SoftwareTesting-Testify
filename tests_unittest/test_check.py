import unittest
from check import Check, Money


class TestCheck(unittest.TestCase):
    def test_check_creation(self):
        check = Check("John Doe", 100)
        self.assertEqual(check.value, 100)
        self.assertEqual(check.payee, "John Doe")

    def test_check_equality(self):
        check1 = Check("John Doe", 100)
        check2 = Check("John Doe", 100)
        self.assertEqual(check1, check2)

    def test_check_inequality(self):
        check1 = Check("John Doe", 100)
        check2 = Check("Jane Doe", 100)
        self.assertNotEqual(check1, check2)


if __name__ == "__main__":
    unittest.main()
