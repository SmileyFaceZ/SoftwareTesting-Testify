"""Testify tests of the Bank Account class."""
from bank_account import BankAccount, CheckError
from check import Check
from testify import TestCase, setup, teardown, assert_equal, assert_raises, run


class BankAccountTest(TestCase):
    """Unit tests of the Bank Account class."""

    @setup
    def setUp(self):
        """Create a test fixture for use in tests."""
        self.account1 = BankAccount("My Bank Account")
        self.check1 = Check("My Bank Account", 10000.0)

    def test_clear_check_only_once(self):
        """Cannot clearing a check more than once."""
        self.account1.deposit(self.check1)
        assert_equal(0, self.account1.available)
        assert_equal(10000.0, self.account1.balance)

        self.account1.clear_check(self.check1)
        assert_equal(10000.0, self.account1.available)
        assert_equal(10000.0, self.account1.balance)

        with assert_raises(CheckError):
            self.account1.clear_check(self.check1)

    @teardown
    def tearDown(self):
        """Remove the test fixture.

        Can be any name method but should be decorated with teardown.
        """
        self.account1 = None
        self.check1 = None


if __name__ == "__main__":
    run()