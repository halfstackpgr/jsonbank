import json
from .pricepool import PricePool
# Limits
MaxLowerLimitVaule=0
# PATHS:
BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"

class Check:
    def AccountExistence(AccountID:str):
        
        
        """
        Source Code:
        
        ```python
        with open(BANK, "r") as file:
            thebank = json.load(file)
        dcheck=list(thebank.keys())
        if AccountID in dcheck:
            return{
                'comment': 'Account Does exist!',
                'result':'Pass'
            }
        else:
            return{
                'comment': 'Account Does not exist!',
                'result':'Fail'
            }
            
        ```
        
        """
        
        
        with open(BANK, "r") as file:
            thebank = json.load(file)
        dcheck=list(thebank.keys())
        if AccountID in dcheck:
            return{
                'comment': 'Account Does exist!',
                'result':'Pass'
            }
        else:
            return{
                'comment': 'Account Does not exist!',
                'result':'Fail'
            }
    
    def Balance(AccountID:str):
        
        
        """
        Source Code:
        
        ```python
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck["result"]=='Pass':
            with open(BANK, "r") as file:
                thebank = json.load(file)
                CurrentBalance=thebank[AccountID][0]["Balance"]
                return{
                    "balance": CurrentBalance,
                    'result': "Pass"
                }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'comment':'Account Not Found !',
                'result': 'Fail'
            }
        ```
        
        """
        
        
        
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck["result"]=='Pass':
            with open(BANK, "r") as file:
                thebank = json.load(file)
                CurrentBalance=thebank[AccountID][0]["Balance"]
                return{
                    "balance": CurrentBalance,
                    'result': "Pass"
                }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'comment':'Account Not Found !',
                'result': 'Fail'
            }

    def SummedBalance()-> None:
        
        
        """
        Source Code:
        
        ```python
        with open(BANK, "r") as file:
            thebank = json.load(file)
        dcheck=thebank.keys()
        NetBalance=[]
        for netOfKeys in dcheck:
            NetBalance.append(thebank[netOfKeys][0]["Balance"])
        return {
            'balance': sum(NetBalance),
            'result':'Pass'
        } 
        ```
        """
        
        
        with open(BANK, "r") as file:
            thebank = json.load(file)
        dcheck=thebank.keys()
        NetBalance=[]
        for netOfKeys in dcheck:
            NetBalance.append(thebank[netOfKeys][0]["Balance"])
        return {
            'balance': sum(NetBalance),
            'result':'Pass'
        }
        
    def IfNegetive(AccountID:str, Amount:int):
        
    
        """
        Source Code:
        
        ```python
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck["result"]=='Pass':
            with open(BANK, "r") as file:
                thebank = json.load(file)
            ExistingBalace=thebank[str(AccountID)][0]["Balance"]
            if ExistingBalace-Amount < 0:
                return {
                    'comment': "Amount Can't be further drawn from this account or it will go below 0, which is not allowed !",
                    'result': 'Fail'
                }
            if ExistingBalace+Amount == 0:
                return {
                    'comment': "Amount Can't be further drawn from this account or it will go 0, which is not allowed !",
                    'result': 'Fail'
                }
            if ExistingBalace+Amount > 0:
                return {
                    'comment': "Amount Can be further drawn from this account !",
                    'result': 'Pass'
                }
            if KeyError:
                return {
                    'comment':"Problem With Finding Account !",
                    "result": "Fail"
                }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'comment':'Account Not Found !',
                'result': 'Fail'
            }
        ```
        """
    

        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck["result"]=='Pass':
            with open(BANK, "r") as file:
                thebank = json.load(file)
            ExistingBalace=thebank[str(AccountID)][0]["Balance"]
            if ExistingBalace-Amount < 0:
                return {
                    'comment': "Amount Can't be further drawn from this account or it will go below 0, which is not allowed !",
                    'result': 'Fail'
                }
            if ExistingBalace+Amount == 0:
                return {
                    'comment': "Amount Can't be further drawn from this account or it will go 0, which is not allowed !",
                    'result': 'Fail'
                }
            if ExistingBalace+Amount > 0:
                return {
                    'comment': "Amount Can be further drawn from this account !",
                    'result': 'Pass'
                }
            if KeyError:
                return {
                    'comment':"Problem With Finding Account !",
                    "result": "Fail"
                }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'comment':'Account Not Found !',
                'result': 'Fail'
            }
        
        

    def AddChecks(AccountID:str, AmountToAdd:int):
        
        
        """
        Source Code:
        
        ```python
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck["result"]=='Pass':
            NetBalaceFlowingRaw=Check.SummedBalance()
            NetBalaceFlowing=NetBalaceFlowingRaw["balance"]
            AmountToAdd=AmountToAdd
            PoolResultRaw=PricePool.check()
            PoolResult=PoolResultRaw['balance']
            CheckingAmount=PoolResult-(NetBalaceFlowing+AmountToAdd)
            if CheckingAmount > 0:
                return {
                    "comment":"Money Can Be Added !",
                    "result": "Pass"
                }
            if CheckingAmount < 0:
                return {
                    "comment":"Limit Exceeds Price Pool !",
                    "result": "Fail"
                }
            if CheckingAmount==0:
                return {
                    "comment":"Money can't be Added. Price Pool Turns 0",
                    "result": "Fail"
                }
            else:
                return {
                    "comment": "An error occured.",
                    'result': "Fail"
                }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'comment':'Account Not Found !',
                'result': 'Fail'
            }
        ```
        
        """
        
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck["result"]=='Pass':
            NetBalaceFlowingRaw=Check.SummedBalance()
            NetBalaceFlowing=NetBalaceFlowingRaw["balance"]
            AmountToAdd=AmountToAdd
            PoolResultRaw=PricePool.check()
            PoolResult=PoolResultRaw['balance']
            CheckingAmount=PoolResult-(NetBalaceFlowing+AmountToAdd)
            if CheckingAmount > 0:
                return {
                    "comment":"Money Can Be Added !",
                    "result": "Pass"
                }
            if CheckingAmount < 0:
                return {
                    "comment":"Limit Exceeds Price Pool !",
                    "result": "Fail"
                }
            if CheckingAmount==0:
                return {
                    "comment":"Money can't be Added. Price Pool Turns 0",
                    "result": "Fail"
                }
            else:
                return {
                    "comment": "An error occured.",
                    'result': "Fail"
                }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'comment':'Account Not Found !',
                'result': 'Fail'
            }

    def DrawChecks(AccountID:str, AmountToDraw:int):
        
        
        """
        Source Code:
        
        ```python
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck["result"]=='Pass':
            CheckResult=Check.IfNegetive(AccountID=AccountID,Amount=AmountToDraw)
            if CheckResult['result']=='Pass':
                return {
                    "comment":"Money Can Be Withdrawn!",
                    "reason": str(CheckResult['comment']),
                    "result": "Pass"
                }
            if CheckResult['result'] =='Fail':
                return {
                    "comment":"Money can't be withdrawn.",
                    "reason": str(CheckResult["comment"]),
                    "result": "Fail"
                }
            else:
                return {
                    "comment": "An error occured.",
                    'result': "Fail"
                }

        if AccountExistenceCheck['result']=='Fail':
            return{
                'comment':'Account Not Found !',
                'reason': "Account Not Found Resitered ! Register an account for yourself !",
                'result': 'Fail'
            }
        ```
        
        """
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck["result"]=='Pass':
            CheckResult=Check.IfNegetive(AccountID=AccountID,Amount=AmountToDraw)
            if CheckResult['result']=='Pass':
                return {
                    "comment":"Money Can Be Withdrawn!",
                    "reason": str(CheckResult['comment']),
                    "result": "Pass"
                }
            if CheckResult['result'] =='Fail':
                return {
                    "comment":"Money can't be withdrawn.",
                    "reason": str(CheckResult["comment"]),
                    "result": "Fail"
                }
            else:
                return {
                    "comment": "An error occured.",
                    'result': "Fail",
                    'reason': str(CheckResult["comment"])
                }

        if AccountExistenceCheck['result']=='Fail':
            return{
                'comment':'Account Not Found !',
                'reason': "Account Not Found Resitered ! Register an account for yourself !",
                'result': 'Fail'
            }

    
    def TransferCheck(fromID:str, toID:str, Amount:int):


        """
        Source Code:
        
        ```python
        AccountExistenceCheckFromID=Check.AccountExistence(AccountID=fromID)
        if AccountExistenceCheckFromID["result"]=='Pass':
            AccountExistenceCheckToID=Check.AccountExistence(AccountID=toID)
            if AccountExistenceCheckToID["result"]=='Pass':
                FromMoneyCheck=Check.DrawChecks(AccountID=fromID, AmountToDraw=Amount)
                if FromMoneyCheck['result']=='Pass':
                    ToMoneyCheck=Check.AddChecks(AccountID=toID, AmountToAdd=Amount)
                    if ToMoneyCheck['result']=='Pass':
                        return {
                            'comment': "Transfer Can Be Granted. Passed All the Checks !",
                            'reason': "Transfer Protocol Passed all the possible checks !s",
                            'result':'Pass'
                        }
                    if ToMoneyCheck['result']=='Fail':
                        return{
                            'comment': 'Account where money is being trasfered has rejected the protocol. Probably cause your transfer will surpass the maximum bank pooling limit!',
                            'reason': str(ToMoneyCheck['comment']),
                            'result': 'Fail'
                        }
                if FromMoneyCheck['result']=='Fail':
                    return{
                        'comment': 'Account from the where the money is being trasnfered has rejected the protocol. Maybe cause of low balance, or you are trying to Transfer more balance than you own!',
                        'reason': str(FromMoneyCheck['comment']),
                        'result': 'Fail'
                    }
            if AccountExistenceCheckToID['result']=='Fail':
                return{
                    'comment': 'Account where money is being trasfered to is not avilable to databases. Create a new!',
                    'reason': str(AccountExistenceCheckToID['comment']),
                    'result': 'Fail'
                }
        if AccountExistenceCheckFromID['result']=='Fail':
            return{
                'comment':'Account that is being used for transfer not found in Database!',
                'reason': "Account Doesn't exists ! Create a new one !",
                'result': 'Fail'
            }
        ```
        
        """
        AccountExistenceCheckFromID=Check.AccountExistence(AccountID=fromID)
        if AccountExistenceCheckFromID["result"]=='Pass':
            AccountExistenceCheckToID=Check.AccountExistence(AccountID=toID)
            if AccountExistenceCheckToID["result"]=='Pass':
                FromMoneyCheck=Check.DrawChecks(AccountID=fromID, AmountToDraw=Amount)
                if FromMoneyCheck['result']=='Pass':
                    ToMoneyCheck=Check.AddChecks(AccountID=toID, AmountToAdd=Amount)
                    if ToMoneyCheck['result']=='Pass':
                        return {
                            'comment': "Transfer Can Be Granted. Passed All the Checks !",
                            'reason': "Transfer Protocol Passed all the possible checks !s",
                            'result':'Pass'
                        }
                    if ToMoneyCheck['result']=='Fail':
                        return{
                            'comment': 'Account where money is being trasfered has rejected the protocol. Probably cause your transfer will surpass the maximum bank pooling limit!',
                            'reason': str(ToMoneyCheck['comment']),
                            'result': 'Fail'
                        }
                if FromMoneyCheck['result']=='Fail':
                    return{
                        'comment': 'Account from the where the money is being trasnfered has rejected the protocol. Maybe cause of low balance, or you are trying to Transfer more balance than you own!',
                        'reason': str(FromMoneyCheck['comment']),
                        'result': 'Fail'
                    }
            if AccountExistenceCheckToID['result']=='Fail':
                return{
                    'comment': 'Account where money is being trasfered to is not avilable to databases. Create a new!',
                    'reason': str(AccountExistenceCheckToID['comment']),
                    'result': 'Fail'
                }
        if AccountExistenceCheckFromID['result']=='Fail':
            return{
                'comment':'Account that is being used for transfer not found in Database!',
                'reason': "Account Doesn't exists ! Create a new one !",
                'result': 'Fail'
            }


    def AccountCreationPooling(Amount:int):
        
        
        """
        Source Code:
        
        ```python
        NetBalaceFlowingRaw=Check.SummedBalance()
        NetBalaceFlowing=NetBalaceFlowingRaw["balance"]
        AmountToAdd=Amount
        PoolResultRaw=PricePool.check()
        PoolResult=PoolResultRaw['balance']
        CheckingAmount=PoolResult-(NetBalaceFlowing+AmountToAdd)
        if CheckingAmount > 0:
            return {
                "comment":"Money Can Be Added !",
                "result": "Pass"
            }
        if CheckingAmount < 0:
            return {
                "comment":"Limit Exceeds Price Pool !",
                "result": "Fail"
            }
        if CheckingAmount==0:
            return {
                "comment":"Money can't be Added. Price Pool Turns 0",
                "result": "Fail"
            }
        else:
            return {
                "comment": "An error occured.",
                'result': "Error"
            }
        ```
        """
        
        NetBalaceFlowingRaw=Check.SummedBalance()
        NetBalaceFlowing=NetBalaceFlowingRaw["balance"]
        AmountToAdd=Amount
        PoolResultRaw=PricePool.check()
        PoolResult=PoolResultRaw['balance']
        CheckingAmount=PoolResult-(NetBalaceFlowing+AmountToAdd)
        if CheckingAmount > 0:
            return {
                "comment":"Balance Can Be Added !",
                "result": "Pass"
            }
        if CheckingAmount < 0:
            return {
                "comment":"New Balance Limit Exceeds Price Pool !",
                "result": "Fail"
            }
        if CheckingAmount==0:
            return {
                "comment":"Balance can't be Added. Price Pool Turns 0",
                "result": "Fail"
            }
        else:
            return {
                "comment": "An error occured.",
                'result': "Error"
            }
