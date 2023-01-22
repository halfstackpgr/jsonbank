import json

# To be only used by Bank Lib!
# Limits
MaxLowerLimitVaule=0
# PATHS:
BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"


class UserGet:
    def UserBalance(AccountID:str):
        ...
    def AccountName(AccountID:str):
        ...
    def BranchName(AccountID:str):
        ...
    def BranchID(AccountID:str):
        ...
    def About(AccountID:str):
        ...



class BankGet:
    def Balance():
        ...
    def Accounts():
        ...
    def Pool():
        ...
        
        
    