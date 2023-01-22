import json

# To be only used by Bank Lib!
# Limits
MaxLowerLimitVaule=0
# PATHS:
BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"


class UserGet:
    def UserBalance(AccountID:str):
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'balance':int(thebank[AccountID][0]["Balance"])
        }
    def AccountName(AccountID:str):
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'name':str(thebank[AccountID][0]["AccountName"])
        }
    def BranchName(AccountID:str):
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'branchname':str(thebank[AccountID][0]["BranchName"])
        }
    def BranchID(AccountID:str):
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'branchid':int(thebank[AccountID][0]["BranchID"])
        }     
    def About(AccountID:str):
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'about':str(thebank[AccountID][0]["About"])
        }
    
        
        


class BankGet:
    def Balance():
        with open(BANK, "r") as file:
            thebank = json.load(file)
        dcheck=thebank.keys()
        NetBalance=[]
        for netOfKeys in dcheck:
            NetBalance.append(thebank[netOfKeys][0]["Balance"])
        return {
            'balance': sum(NetBalance),
        }
    def Accounts():
        with open(BANK, "r") as file:
            thebank = json.load(file)
        dcheck=thebank.keys()
        NetBalance=[]
        for netOfKeys in dcheck:
            NetBalance.append(thebank[netOfKeys])
        return {
            'accounts': len(NetBalance),
        }
    def Pool():
        with open(POOLING, "r") as file:
            Pool = json.load(file)
        return {
            "balance": Pool["maximum"]
        }
    def RemainingPool():
        
        PoolLatest=BankGet.Pool()['balance']
        UsedPool=BankGet.Balance()['balance']
        RemainingPool=PoolLatest-UsedPool
        return{
            'leftpool':RemainingPool
        }
