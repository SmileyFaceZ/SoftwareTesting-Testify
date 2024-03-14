# BankAccount Module

This module defines the `BankAccount` class and the `CheckError` exception.

## BankAccount Class

The `BankAccount` class represents a bank account that accepts deposits of money or checks and allows withdrawals of money.

The BankAccount class is used for modeling bank accounts, providing functionalities to manage deposits, withdrawals, and checks associated with an account. It serves as a representation of a user's financial account within a banking system.

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

---

# Check Class

The `Check` class represents a check with a specified value, payee (recipient), and a unique serial number.

The Check class is used for representing checks, which are financial instruments that serve as a claim for a specified amount of money. 

## Check Class Features:

- Inherits from the `Money` class.
- Provides functionalities for adding checks and money, comparison operations, and string representations.
- Each check has a unique serial number assigned automatically.
- Checks use the default currency of `Money` for simplicity.

### Attributes:

- `payee`: Name of the recipient of the check.
- `check_number`: Unique serial number assigned to the check.

### Methods:

- `__init__(self, payee_name: str, amount: float)`: Initializes a new check with the given payee and amount.
- `__eq__(self, other)`: Compares two checks based on their value and check number.
- `__str__(self)`: Returns the string representation of a check.
- `__repr__(self)`: Returns the string representation of a check.

---

# Money Module

This module defines the `Money` class, which represents a monetary value with a specified currency. The class provides various functionalities for performing arithmetic operations and comparisons on money objects.

## Money Class

The `Money` class is an immutable object with a value and currency. It supports addition, subtraction, and comparison operations between money objects.

The Money class is used for representing monetary values with associated currencies. It allows for performing arithmetic operations such as addition and subtraction between money objects of the same currency. Additionally, it supports comparison operations to compare the values of money objects, disregarding their currencies.

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

---

## Scenario 1: Deposit Cash Correctly Adds to Balance and Available Balance

**Precondition:** 
- Account is created with initial 0.0 balance.

**Step:**
1. User deposits cash.

**Expected Result:**
- Balance increases by the cash amount.
- Available balance increases by the cash amount.

## Scenario 2: Cannot Withdraw More Than the Balance in Account

**Precondition:** 
- Account is created.
- User deposits some money.

**Step:**
1. User deposits cash.
2. User attempts to withdraw money more than the balance.

**Expected Result:**
- Raises ValueError.

## Scenario 3: Cannot Clear a Check More Than Once

**Precondition:** 
- Account is created.
- Check is created.

**Step:**
1. User deposits a check in the account.
2. Balance increases.
3. User clears the check.
4. Available balance increases.
5. User attempts to clear the check again.

**Expected Result:**
- Raises CheckError.

