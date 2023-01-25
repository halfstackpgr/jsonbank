### JSON BANK
A random brain stormed Idea I got after experimenting with Hikari and Lightbulb to make discord bots. 
```python
print("Welcome To JSON Bank !")
```
<div align="center">
    <img src="https://cdn-wordpress-info.futurelearn.com/wp-content/uploads/how-does-the-economy-work-606x303.jpg.webp">
</div>

*This idea happened to strike my brain when I was trying to figure out a way to make an Economy Bot, but I am lazy enough not to learn operational databases, and hence I decided to make it using JSONs, now the idea was limited to make a bot for my server, but instead I made a library so that everyone can use it. Making their own Economy Bots*


Tested with:
```python
pip install hikari-lightbulb
```

> This library right now, is in the best stable stage with all the "Source" docstrings attached to it. The Bank.py returns two request codes with comment or result. They are 
**200** *for every successfull attempt using a function*
**and**
**400** *for every unsucessfull attempt using a function*


Some Upcoming Features and already added features:

>Account creation: The ability to create new bank accounts, including setting an account name, ID, and initial balance. **done**
>Account balance: The ability to check the current balance of an account. **done**
>Deposits and withdrawals: The ability to deposit and withdraw money from an account.  **done**
>Transfer money: The ability to transfer money between accounts.  **done**
>Transactions history: The ability to view a list of past transactions for an account, including deposits, withdrawals, and transfers.  **In Future**
>Interest and Fees: Ability to add interest and fees to an account. **Can be done using the bot, and scheduler**
>Multi-user support: The ability to handle multiple users and accounts at the same time.**done**
>Authentication: Implementing a secure way of authenticating users and their accounts. **In Future !**
>Error Handling: Handling exceptions and errors when invalid inputs are given or when an account does not have enough funds for a withdrawal. **done**
>Reports: Generating reports on account balances, transactions and other banking activities. **Can be done using the bot, and scheduler using dict handlers**


