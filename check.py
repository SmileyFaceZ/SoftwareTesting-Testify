"""Check is a claim for a specified about of Money, with a serial number."""
from money import Money


class Check(Money):
    """
    A check with a value and an auto-generated serial number.
    Payee is the person to whom the check is written and can deposit it.
    Check is a form of Money, so you can add Checks and Money.
    The result of addition (+) is always Money.
    If you compare Checks using == it will compare the value,
    currency, AND the serial number.  So two Check objects
    are equal only if value, currency, and serial number are same.

    >>> c = Check('Bill Gates', 5000)
    >>> c.value
    5000
    >>> c.payee
    'Bill Gates'
    >>> str(c)
    'Check number 1000000 for 5,000 Baht'
    >>> m = Money(200)
    >>> str(c+m)             # addition is inherited from Money
    '5,200 Baht'
    >>> c > m
    True
    >>> c2 = Check(c.payee, c.value)  # same value, different check number
    >>> c == c2
    False
    """
    # Class attribute for next available serial number.
    __next_check_number = 1000000

    def __init__(self, payee_name: str, amount: float):
        """A new check with a given amount and payee (the receiver).

        A unique check number is assigned automatically.
        For simplicity, checks always use the default currency of Money.

        :param payee_name: name of intended recipient of the check
        :param amount: the value of the check
        """
        if amount < 0:
            raise ValueError("Check value cannot be negative.")
        super().__init__(amount)
        self.__payee = payee_name
        self.__number = Check.__next_check_number
        Check.__next_check_number += 1

    @property
    def check_number(self) -> int:
        """The check number, a unique integer."""
        return self.__number

    @property
    def payee(self) -> str:
        """Name of the recipient of this check."""
        return self.__payee

    def __eq__(self, other):
        """Two checks are equal if they have same value and check number."""
        if not isinstance(other, Check):
            return False
        return self.check_number == other.check_number and self.value == other.value

    def __str__(self):
        """String representation of a check."""
        return f"Check number {self.__number:d} for {super().__str__()}"

    def __repr__(self):
        """String representation of a check."""
        return f"Check('{self.__payee}', {self.value})"
