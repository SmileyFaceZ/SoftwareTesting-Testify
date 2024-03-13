from testify import TestCase, assert_equal, assert_not_equal
from check import Check, Money


class TestCheck(TestCase):
    def test_check_creation(self):
        check = Check("John Doe", 100)
        assert_equal(check.value, 100)
        assert_equal(check.payee, "John Doe")

    def test_check_equality(self):
        check1 = Check("John Doe", 100)
        check2 = Check("John Doe", 100)
        assert_equal(check1, check2)

    def test_check_inequality(self):
        check1 = Check("John Doe", 100)
        check2 = Check("Jane Doe", 100)
        assert_not_equal(check1, check2)


if __name__ == "__main__":
    run()
