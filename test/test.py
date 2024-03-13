from bank_account import BankAccount, CheckError
from check import Check
from money import Money
from testify import *

class CashTestCase(TestCase):
    """Unit tests of the Bank Account class."""
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

    def test_deposit_zero_amount(self):
        """Deposit zero money should raise ValueError."""
        with assert_raises(ValueError):
            self.account1.deposit(Money(0.0))

    def test_overwithdraw(self):
        """Cannot withdraw more than the balance in account."""
        self.account1.deposit(Money(1000.0))
        withdrawal = self.account1.withdraw(1.0)
        assert_not_equal(withdrawal, None)
        assert_equal(1.0, withdrawal.value)
        assert_equal(999.0, self.account1.balance)
        with assert_raises(ValueError):
            withdrawal = self.account1.withdraw(1000)


    def test_available_balance(self):
        """Clearing a check should increase available balance."""
        assert_equal(0, self.account1.balance)
        assert_equal(0, self.account1.available)

        self.account1.deposit(Money(1000.0))
        assert_equal(1000.0, self.account1.balance)
        assert_equal(1000.0, self.account1.available)

        self.account1.deposit(self.check1)
        assert_equal(11000.0, self.account1.balance)
        assert_equal(1000.0, self.account1.available)

        self.account1.clear_check(self.check1)
        assert_equal(11000.0, self.account1.balance)
        assert_equal(11000.0, self.account1.available)

    def test_withdraw_all_money(self):
        """Withdraw all money in the account."""
        self.account1.deposit(Money(1500.0))
        assert_equal(1500.0, self.account1.available)

        self.account1.withdraw(1500)
        assert_equal(0, self.account1.available)



class CheckTestCase(TestCase):
    """Unit tests of the Bank Account class."""
    def setUp(self):
        """Create a test fixture for use in tests."""
        self.account1 = BankAccount("My Bank Account")
        self.check1 = Check("My Bank Account", 10000.0)
        self.check2 = Check("Bank Account", 500.0)

    def test_deposit_check_only_once(self):
        """Cannot deposit the same check twice."""
        self.account1.deposit(self.check1)
        assert_equal(0, self.account1.available)

        self.account1.clear_check(self.check1)
        assert_equal(10000.0, self.account1.available)
        with assert_raises(CheckError):
            self.account1.deposit(self.check1)

    def test_deposit_check_twice(self):
        """Cannot deposit the check twice"""
        check = Check('My Bank Account',100)
        with assert_raises(CheckError):
            self.account1.deposit(check)
            self.account1.deposit(check)

    def test_cannot_withdraw_money_with_deposit_check_only(self):
        """Cannot withdraw money with deposit check only."""
        self.account1.deposit(self.check1)
        assert_equal(0, self.account1.available)
        assert_equal(10000.0, self.account1.balance)

        with assert_raises(ValueError):
            self.account1.withdraw(1000)

    def test_deposit_check_with_different_payee(self):
        """Cannot deposit check with different payee."""
        with assert_raises(CheckError):
            self.account1.deposit(self.check2)


if __name__ == "__main__":
    run()