from testify import TestCase, assert_equal
from bank_account import BankAccount, CheckError, Check
from money import Money


class TestBankAccount(TestCase):
    def test_deposit_money(self):
        account = BankAccount("John Doe")
        account.deposit(Money(100))
        assert_equal(account.balance, 100)

    def test_withdraw_money(self):
        account = BankAccount("John Doe")
        account.deposit(Money(100))
        account.withdraw(50)
        assert_equal(account.balance, 50)

    def test_withdraw_raises_error_if_insufficient_funds(self):
        account = BankAccount("John Doe")
        account.deposit(Money(100))
        with self.assertRaises(ValueError):
            account.withdraw(150)

    def test_clear_check_raises_error_if_check_not_deposited(self):
        account = BankAccount("John Doe")
        check = Check("John Doe", 100)
        with self.assertRaises(CheckError):
            account.clear_check(check)


if __name__ == "__main__":
    run()
