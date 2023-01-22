### JSON BANK
A random brain stormed Idea I got after experimenting with Hikari and Lightbulb to make discord bots. 
```python
print("Welcome to Your Very Own Economy Bot Data Handler System.")
```
<div align="center">
    <img src="https://cdn-wordpress-info.futurelearn.com/wp-content/uploads/how-does-the-economy-work-606x303.jpg.webp">
</div>

*The idea was to build an economy bot for my server which turned to making a handler, which is now I am making avilable to public so that they can use it as well, to personalise their own bot.*


Tested with:
```python
pip install hikari-lightbulb
```
>This library is not even in testing stage, neither I claim it to be in, I am just experementing with my kowledge. + This library won't be much of a benefit if you are building a commerical bot for like 10,000+ people. Since It requires local storage. 


Important Code Block:

```python
    def checkIfNegetiveAddition(AccountID:str, Amount:int):
        with open(BANK, "r") as file:
            thebank = json.load(file)
        ExistingBalace=thebank[str(AccountID)][0]["Balance"]
        if ExistingBalace+Amount < 0:
            return "NOT OK"
        if ExistingBalace+Amount == 0:
            return 0
        if ExistingBalace+Amount > 0:
            return "OK"
    def checkIfNegetiveBalanceWithdrawl(AccountID:str, Amount:int):
        with open(BANK, "r") as file:
            thebank = json.load(file)
        ExistingBalace=thebank[str(AccountID)][0]["Balance"]
        if ExistingBalace-Amount < 0:
            return "NOT OK"
        if ExistingBalace-Amount == 0:
            return 0
        if ExistingBalace-Amount > 0:
            return "OK"
```
Some Upcoming Features and already added features:

>Account creation: The ability to create new bank accounts, including setting an account name, ID, and initial balance.

>Account balance: The ability to check the current balance of an account.

>Deposits and withdrawals: The ability to deposit and withdraw money from an account.

>Transfer money: The ability to transfer money between accounts.

>Transactions history: The ability to view a list of past transactions for an account, including deposits, withdrawals, and transfers.

>Interest and Fees: Ability to add interest and fees to an account.

>Multi-user support: The ability to handle multiple users and accounts at the same time.

>Authentication: Implementing a secure way of authenticating users and their accounts.

>Error Handling: Handling exceptions and errors when invalid inputs are given or when an account does not have enough funds for a withdrawal.

>Reports: Generating reports on account balances, transactions and other banking activities.
