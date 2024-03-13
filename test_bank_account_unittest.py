"""Unit tests of the Bank Account class."""
import unittest
from bank_account import BankAccount, CheckError
from check import Check
from money import Money


class BankAccountTest(unittest.TestCase):
    """Unit tests of the Bank Account class."""

    def setUp(self):
        """Create a test fixture for use in tests.

        Must be named setUp."""
        self.account1 = BankAccount("My Bank Account")
        self.check1 = Check("My Bank Account", 10000.0)

    # def test_deposit_cash(self):  #
    #     """Deposit cash correctly adds to balance and available balance."""
    #     self.assertEqual(4, 2)
        # self.assertEqual(0.0, self.account1.balance)
        # total_amount = 0
        # for amount in [0.01, 1, 1000]:
        #     total_amount += amount
        #     self.account1.deposit(Money(amount))
        #     self.assertEqual(total_amount, self.account1.balance)
        #     self.assertEqual(total_amount, self.account1.available)

    # def test_deposit_zero_amount(self):  #
    #     """Deposit zero money should raise ValueError."""
    #     with self.assertRaises(ValueError):
    #         self.account1.deposit(Money(0.0))
    #
    def test_overwithdraw(self):  #
        """Cannot withdraw more than the balance in account."""
        self.account1.deposit(Money(1000.0))
        withdrawal = self.account1.withdraw(1.0)
        self.assertIsNotNone(withdrawal)
        self.assertEqual(1.0, withdrawal.value)
        self.assertEqual(999.0, self.account1.balance)
        with self.assertRaises(ValueError):
            withdrawal = self.account1.withdraw(1000)
    #
    # def test_clear_check_only_once(self):  #
    #     """Cannot clearing a check more than once."""
    #     self.account1.deposit(self.check1)
    #     self.assertEqual(0, self.account1.available)
    #     self.assertEqual(10000.0, self.account1.balance)
    #
    #     self.account1.clear_check(self.check1)
    #     self.assertEqual(10000.0, self.account1.available)
    #     self.assertEqual(10000.0, self.account1.balance)
    #
    #     with self.assertRaises(CheckError):
    #         self.account1.clear_check(self.check1)
    #
    # def test_available_balance(self):  #
    #     """Clearing a check should increase available balance."""
    #     self.assertEqual(0, self.account1.balance)
    #     self.assertEqual(0, self.account1.available)
    #
    #     self.account1.deposit(Money(1000.0))
    #     self.assertEqual(1000.0, self.account1.balance)
    #     self.assertEqual(1000.0, self.account1.available)
    #
    #     self.account1.deposit(self.check1)
    #     self.assertEqual(11000.0, self.account1.balance)
    #     self.assertEqual(1000.0, self.account1.available)
    #
    #     self.account1.clear_check(self.check1)
    #     self.assertEqual(11000.0, self.account1.balance)
    #     self.assertEqual(11000.0, self.account1.available)
    #
    # def test_withdraw_all_money(self):
    #     """Withdraw all money in the account."""
    #     self.account1.deposit(Money(1500.0))
    #     self.assertEqual(1500.0, self.account1.available)
    #
    #     self.account1.withdraw(1500)
    #     self.assertEqual(0, self.account1.available)
    #
    # def test_deposit_check_only_once(self):
    #     """Cannot deposit the same check twice."""
    #     self.account1.deposit(self.check1)
    #     self.assertEqual(0, self.account1.available)
    #
    #     self.account1.clear_check(self.check1)
    #     self.assertEqual(10000.0, self.account1.available)
    #     with self.assertRaises(CheckError):
    #         self.account1.deposit(self.check1)
    #
    # def test_cannot_withdraw_money_with_deposit_check_only(self):
    #     """Cannot withdraw money with deposit check only."""
    #     self.account1.deposit(self.check1)
    #     self.assertEqual(0, self.account1.available)
    #     self.assertEqual(10000.0, self.account1.balance)
    #
    #     with self.assertRaises(ValueError):
    #         self.account1.withdraw(1000)
    #
    # def test_deposit_check_with_different_payee(self):
    #     """Cannot deposit check with different payee."""
    #     with self.assertRaises(CheckError):
    #         self.account1.deposit(self.check2)
    #
    # def tearDown(self):
    #     """Remove the test fixture.
    #
    #     Must be named tearDown."""
    #     self.account1 = None
    #     self.check1 = None