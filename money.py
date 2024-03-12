"""Money with a value and currency.

Overload the operators > and >= and you get < and <= for free,
since Python automatically reverses direction of comparison
when only one operator is explicitly overloaded.
"""
import re

DEFAULT_CURRENCY = "Baht"
# regular expression for valid currencies
CURRENCY_REGEX = "[A-Z][A-Za-z]+"


class Money:
    """Money is an immutable object with a value and currency.

    You can add Money objects that have the same currency,
    including Checks (a subclass), and the result is Money.
    You can compare Money using ==, <, and <= so you can write:

    >>> total = Money(500) + Money(100)
    >>> total == Money(600)
    True
    >>> m = Money(1100)
    >>> m.value
    1100
    >>> str(m)
    '1,100 Baht'
    >>> m2 = m + Money(1)
    >>> m2 > m
    True
    >>> m2 = m2 - Money(1)
    >>> m >= m2
    True
    >>> m + Money(5, "USD")
    Traceback (most recent call last):
      ...
    ValueError: Cannot add money with different currencies
    >>> m.value = 999   # change the value?
    Traceback (most recent call last):
     ...
    AttributeError: can't set attribute

    >>> m3 = Money(1000, "***")
    Traceback (most recent call last):
      ...
    ValueError: Invalid Currency

    >>> m - Money(100, "USD")
    Traceback (most recent call last):
      ...
    ValueError: Cannot subtract money with different currencies

    >>> m == "Money(100)"
    False
    >>> m4 = Money(123.25)
    >>> str(m4)
    '123.25 Baht'
    >>> Money(100)
    'Money(100, 'Baht')'
    """

    def __init__(self, value: float, currency: str = DEFAULT_CURRENCY):
        """Initialize a new money object with given value.

        :param value: value of Money, a number.
        :param currency: currency, a string of at least 2 chars.
        :raises ValueError: if currency is not a string
               containing only 2 or more alphabetic characters
               starting with a capital letter.
        """
        if not re.fullmatch(CURRENCY_REGEX, currency):
            raise ValueError("Invalid Currency")
        self.__value = value
        self.__currency = currency

    @property
    def value(self) -> float:
        """Return the value of this Money, as a number."""
        return self.__value

    @property
    def currency(self) -> str:
        """Return the currency of this Money object."""
        return self.__currency

    def __add__(self, money):
        """Add a money object to this one and return the sum."""
        if self.currency.lower() != money.currency.lower():
            raise ValueError("Cannot add money with different currencies")
        return Money(self.__value + money.__value, self.currency)

    def __sub__(self, money):
        """Subtract a money object from this one and return the difference."""
        if self.currency.lower() != money.currency.lower():
            raise ValueError("Cannot subtract money with different currencies")
        return Money(self.__value - money.__value, self.currency)

    def __gt__(self, money):
        """Compare money objects by value, ignoring currency.

        >>> Money(100) > Money(101)
        False
        >>> Money(101) > Money(100)
        True
        >>> Money(100) > Money(100)
        False
        >>> Money(100.01) > Money(100)
        True
        """
        return self.__value > money.__value

    def __ge__(self, money):
        """Compare money objects by value, ignoring currency.

        >>> Money(100) >= Money(101)
        False
        >>> Money(101) >= Money(100)
        True
        >>> Money(100) >= Money(100)
        True
        """
        return self.__value >= money.__value

    def __eq__(self, other):
        """Two money instances equal if both value and currency are same."""
        if not isinstance(other, Money):
            return False
        return (self.value == other.value and
                self.currency.lower() == other.currency.lower())

    def __str__(self):
        """Formatted string value of Money, include decimals only if needed."""
        if int(self.__value) == self.__value:
            return f"{self.__value:,.0f} {self.__currency}"
        return f"{self.__value:,.2f} {self.__currency}"

    def __repr__(self):
        """Representation of Money, including value and currency."""
        return f"{type(self).__name__}({self.__value}, '{self.__currency}')"


if __name__ == '__main__':  # pragma: no cover
    import doctest
    doctest.testmod()
