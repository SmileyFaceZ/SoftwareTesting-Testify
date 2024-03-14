# BankAccount Module

This module defines the `BankAccount` class and the `CheckError` exception.

## BankAccount Class

The `BankAccount` class represents a bank account that accepts deposits of money or checks and allows withdrawals of money.

### Attributes:

- `name`: Name of the account owner.
- `balance`: Current balance in the account.
- `min_balance`: Minimum required balance for the account (default is 0).
- `pending_checks`: List of checks deposited but not yet cleared.

### Methods:

- `__init__(self, name: str, min_balance: float = 0.0)`: Initializes a new bank account with the given name and minimum balance.
- `deposit(self, money: Money)`: Deposits money or a check into the account.
- `withdraw(self, amount: float) -> Money`: Withdraws an amount from the account.
- `clear_check(self, check: Check)`: Marks a check as cleared so it is available for withdrawal.
- `__str__(self)`: Returns a string representation of the bank account.

### Properties:

- `account_name`: Returns the name of the account.
- `available`: Returns the available balance in the account.
- `balance`: Returns the current balance in the account.
- `min_balance`: Returns the minimum required balance for the account.

# Money Module

This module defines the `Money` class, which represents a monetary value with a specified currency. The class provides various functionalities for performing arithmetic operations and comparisons on money objects.

## Money Class

The `Money` class is an immutable object with a value and currency. It supports addition, subtraction, and comparison operations between money objects.

### Attributes:

- `value`: The value of the money object.
- `currency`: The currency of the money object.

### Methods:

- `__init__(self, value: float, currency: str = DEFAULT_CURRENCY)`: Initializes a new money object with the given value and currency.
- `__add__(self, money)`: Adds a money object to this one and returns the sum.
- `__sub__(self, money)`: Subtracts a money object from this one and returns the difference.
- `__gt__(self, money)`: Compares money objects by value, ignoring currency (greater than).
- `__ge__(self, money)`: Compares money objects by value, ignoring currency (greater than or equal to).
- `__eq__(self, other)`: Checks if two money instances are equal based on both value and currency.
- `__str__(self)`: Returns the formatted string value of money, including decimals only if needed.
- `__repr__(self)`: Returns the representation of money, including value and currency.

## CheckError Exception

The `CheckError` exception is raised for invalid operations on checks.

This module provides functionality for managing bank accounts, handling deposits and withdrawals, as well as dealing with checks and their clearance.
