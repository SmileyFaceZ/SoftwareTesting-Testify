"""Testify tests of the Bank Account class."""
from bank_account import BankAccount
from check import Check
from money import Money


from testify import (TestCase, setup, teardown, assert_equal, assert_raises,
                    run)

class BankAccountTest(TestCase):
    """Unit tests of the Bank Account class."""

    @setup
    def setUp(self):
        """Create a test fixture for use in tests."""
        self.account1 = BankAccount("My Bank Account")
        self.check1 = Check("My Bank Account", 10000.0)

    def test_overwithdraw(self):
        """Cannot withdraw more than the balance in account."""
        self.account1.deposit(Money(1000.0))
        withdrawal = self.account1.withdraw(1.0)
        assert_equal(1.0, withdrawal.value)
        assert_equal(999.0, self.account1.balance)
        with assert_raises(ValueError):
            withdrawal = self.account1.withdraw(1000)

    @teardown
    def tearDown(self):
        """Remove the test fixture."""
        self.account1 = None
        self.check1 = None


if __name__ == "__main__":
    run()