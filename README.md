## Unit Testing Problem

Write unit tests for the BankAccount class in the file `bank_account.py`.    
Put your tests in a file named `test_bank_account.py`.

Problem description is given on the web.

1. Write tests for the *specification* not the actual BankAccount code.
2. Write tests to verify *any* BankAccount code that has the same methods -- not just the sample code.
3. Write enough tests for the specification but please don't write redundant tests.
4. Tests should not access attributes of BankAccount or depend on details of the implementation.
5. You do not need to test these trivial things:
   - `min_balance` property
   - `__str__` method
6. It is OK to use more than one `assert` per test method.

## What to Submit

Push your code, including `test_bank_account.py` and your answers in README.md.

When you push to Github, it will run your tests against several implementations of BankAccount containing various bugs.  

Try to detect all defects and identify the likely cause of the defect.

## Analysis of Errors in Bank Account Variants

Include
- what method in BankAccount appears to be in error
- possible cause or causes of the error, such as failure to test some condition
- if no error in variant code, write "No defects"

| Variant # | Description of Underlying Error                               |
|-----------|---------------------------------------------------------------|
|     1     | Cannot Withdraw all money in the account.                     |
|     2     | Cannot withdraw more than the balance in account.             |
|     3     | Cannot deposit zero money.                                    |
|     4     | Cannot clearing a check more than once.                       |
|     5     | Cannot deposit the same check twice.                          |
|     6     | Cannot deposit check with different payee.                    |
|     7     | Clearing a check should increase available balance.           |
|     8     | Deposit cash correctly adds to balance and available balance. |
