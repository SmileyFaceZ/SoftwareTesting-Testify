from bank_account import BankAccount, CheckError
from check import Check
from money import Money

"""Doctests of bank account.

>>> acct = BankAccount("Bill Gates")  # account owner is 'Bill Gates'
>>> acct.balance
0.0
>>> acct.available
0.0
>>> acct.min_balance
0.0
>>> acct.deposit( Money(20000) )   # deposit 20,000 cash
>>> acct.balance
20000.0
>>> acct.available
20000.0
>>> acct.withdraw(10000)           # withdraw 10,000 Baht
Money(10000, 'Baht')
>>> acct.balance
10000.0
>>> c = Check("Bill Gates", 5000)  # deposit a check payable to 'Bill Gates'
>>> acct.deposit(c)
>>> acct.balance
15000.0
>>> acct.available                 # check has not cleared yet, so value is not available
10000.0
>>> acct.withdraw(12000)           # try to withdraw it anyway
Traceback (most recent call last):
   ...
ValueError: Amount exceeds available balance
>>> acct.clear_check(c)            # clear check so its value is available for withdraw
>>> acct.available
15000.0
>>> acct.withdraw(12000)           # withdraw 12,000 should work now
Money(12000, 'Baht')
>>> acct.balance
3000.0
>>> acct.withdraw(4000)            # can we withdraw more than the balance?
Traceback (most recent call last):
   ...
ValueError: Amount exceeds available balance
>>> acct.withdraw(2000)            # can we withdraw 2,000?
Money(2000, 'Baht')
>>> acct.balance                   # withdrew 12,000 + 2,000. Should be 1,000 remaining. 
1000.0
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
