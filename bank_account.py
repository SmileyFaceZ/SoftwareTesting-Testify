"""Module that defines BankAccount and CheckError."""
from money import Money
from check import Check


class BankAccount:
    """
    A BankAccount that accepts deposits of Money or Checks and withdraw of money.

    A BankAccount has a balance and may have a minimum required balance (default 0).
    The balance is always the total value of money and checks in the account,
    but the value of a check is not available for withdraw until
    `clear_check(check)` is called to "clear" the check.
    The "available balance" is the maximum that can be withdrawn.
    Available balance is the total balance minus the value of uncleared
    checks and any minimum balance requirement.
    """

    def __init__(self, name: str, min_balance: float = 0.0):
        """Create a new account with given name.

        :param name: the name of the account owner
        :min_balance: the minimum required balance, a non-negative number.
                Default min balance is zero.
        """
        # you don't need to test min_balance < 0. It's too trivial.
        assert min_balance >= 0, "min balance parameter must not be negative"
        self.__name = name
        self.__balance = 0.0
        self.__min_balance = float(min_balance)
        # checks deposited and waiting to be cleared
        self.__pending_checks = []

    @property
    def account_name(self):
        """Name of the account cannot be changed."""
        return self.__name

    @property
    def available(self) -> float:
        """Available balance in this account, as a number.

        Available balance is the maximum that can be withdrawn without either:
        (a) balance becoming less than min_balance, or
        (b) balance being less than the value of uncleared checks.
        """
        sum_holds = sum(check.value for check in self.__pending_checks)
        avail = self.balance - self.min_balance - sum_holds
        return avail if (avail > 0) else 0.0

    @property
    def balance(self) -> float:
        """Balance in the account as a value without a currency."""
        return self.__balance

    def clear_check(self, check: Check):
        """Mark a check as cleared so it is available for withdraw.

        :param check: reference to a previously deposited check.
        :raises CheckError: if the check is not in the list of uncleared checks
        """
        if check not in self.__pending_checks:
            raise CheckError(
                f"Check {check.check_number} is not an uncleared check"
            )

        self.__pending_checks.remove(check)

    def deposit(self, money: Money):
        """Deposit money or check into the bank account.

        :param money: Money or Check object with a positive value.
        :raises ValueError: if value of money parameter is not positive.
        :raises TypeError: if the parameter is not money.
        :raises CheckError: if parameter is a check that cannot be deposited.
        """
        if not isinstance(money, Money):
            raise TypeError("Parameter must be type money")
        if money.value <= 0:
            raise ValueError("Cannot deposit a negative amount")
        # if it is a check, verify the check was not already deposited
        if isinstance(money, Check):
            check = money
            if check.payee != self.__name:
                raise CheckError(
                    "Cannot deposit a check with the same payee "
                    "and bank account"
                )
            if check in self.__pending_checks:
                raise CheckError("Check already deposited")

            # add to list of checks waiting to clear
            self.__pending_checks.append(check)
        # both cash and checks contribute to the balance
        self.__balance += money.value

    @property
    def min_balance(self) -> float:
        """Minimum required balance for this account."""
        return self.__min_balance

    def withdraw(self, amount: float) -> Money:
        """Withdraw an amount from the account.

        :param amount: (number) the amount to withdraw, at most the available balance.
        :returns: a Money object for the amount requested, using the default currency.
        :raises ValueError: if amount exceeds available balance or is not positive.
        """
        if amount <= 0:
            raise ValueError("Amount to withdraw must be positive")
        if amount >= self.available:
            raise ValueError("Amount exceeds the available balance")
        # try to create the money before deducting from balance,
        # in case Money throws an exception.
        money = Money(amount)
        self.__balance -= amount
        return money

    def __str__(self):
        """String representation of the bank account."""
        return f"{self.account_name} Account"


class CheckError(Exception):
    """Exception raised by invalid operation on checks."""
    # all behavior is inherited from the superclass
    pass
