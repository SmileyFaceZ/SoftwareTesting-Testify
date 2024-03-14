"""Testify tests of the Bank Account class."""
from bank_account import BankAccount
from check import Check
from money import Money

from testify import TestCase, setup, teardown, assert_equal, run


class BankAccountTest(TestCase):
    """Unit tests of the Bank Account class."""

    @setup
    def setUp(self):
        """Create a test fixture for use in tests."""
        self.account1 = BankAccount("My Bank Account")
        self.check1 = Check("My Bank Account", 10000.0)

    def test_deposit_cash(self):
        """Deposit cash correctly adds to balance and available balance."""
        assert_equal(0.0, self.account1.balance)
        total_amount = 0
        for amount in [0.01, 1, 1000]:
            total_amount += amount
            self.account1.deposit(Money(amount))
            assert_equal(total_amount, self.account1.balance)
            assert_equal(total_amount, self.account1.available)

    @teardown
    def tearDown(self):
        """Remove the test fixture.

        ensuring that the test environment is reset to a known state before
        the next test method is run.
        """
        self.account1 = None
        self.check1 = None


if __name__ == "__main__":
    run()