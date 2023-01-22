import json
import datamanagers.converters
import datamanagers.updaters
import modals.pricepool
import modals.checks
from datamanagers.converters import Converters, AllResults
from datamanagers.updaters import Update
from modals.checks import Check
from modals.pricepool import PricePool


MaxLowerLimitVaule=0
# PATHS:
BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"


def CreateAccount(
    AccountID:str="999",
    AccountName:str="Default",
    BranchName:str = "HalfStackPgr",
    BranchID:int =0,
    Balance:int = 0,
    About:str = "Account Created"
    ):
    CheckingAccountExistence=Check.AccountExistence(AccountID=AccountID)
    if CheckingAccountExistence['result']=='Fail':
        CheckingPoolingData=Check.AccountCreationPooling(Amount=Balance)
        if CheckingPoolingData['result']=='Pass':
            
            with open(BANK, "r") as file:
                thebank = json.load(file)
                newAc= {
                AccountID:[
                    {
                    "AccountName": AccountName,
                    "AccountID": AccountID,
                    "CreatedGuildName": BranchName,
                    "CreatedGuildID": BranchID,
                    "Balance": Balance,
                    "About": About
                    }
                ]
            }
                thebank.update(newAc)
                with open(BANK, "w") as file:
                    json.dump(thebank, file, indent=2)
                return {
                    "comment":f"Account Registered into the Bank Portal with {Balance} as balance !",
                    "result": 200
                }
        if CheckingPoolingData['result']=='Fail':
            return{
                'result': 400,
                'comment': str(CheckingPoolingData['comment'])
            }
    if CheckingAccountExistence['result']=='Pass':
        with open(BANK, "r") as file:
            thebank = json.load(file)
        with open(BANK, "r") as file:
            thebank = json.load(file)
        ExistingAccountHolderName=thebank[AccountID][0]["AccountName"]
        return {
            "comment":f"Accout Already exists with the ID: {AccountID} and has the holder name as: {ExistingAccountHolderName}",
            "result": 400
            }

def AddMoney(AccountID:str, Amount:int):
    AddMoneyCheck=Check.AddChecks(AccountID=AccountID,AmountToAdd=Amount)
    if AddMoneyCheck['result']=='Pass':
        Update.addmoney(AccountID=AccountID, AmountToAdd=Amount)
        return{
            'comment': "Amount successfully added !",
            'result': 200,
            'reason': str(AddMoneyCheck['reason'])
        }
    if AddMoneyCheck['result']=='Fail':
        return{
            'comment': "Amount Could Not Be Added !",
            'result': 400,
            'reason': str(AddMoneyCheck['reason'])
        }
    else:
        return{
            'comment': "Unknown Error While Processing Request!",
            'result': 400,
            'reason': str(AddMoneyCheck['reason'])
        }


def DrawMoney(AccountID:str, Amount:int):
    DrawMoneyCheck=Check.DrawChecks(AccountID=AccountID,AmountToDraw=Amount)
    if DrawMoneyCheck['result']=='Pass':
        Update.drawmoney(AccountID=AccountID, AmountToWithDraw=Amount)
        return{
            'comment': "Amount successfully drawn !",
            'result': 200,
            'reason': str(DrawMoneyCheck['reason'])
        }
    if DrawMoneyCheck['result']=='Fail':
        return{
            'comment': "Amount Could Not Be Drawn from the account! !",
            'result': 400,
            'reason': str(DrawMoneyCheck['reason'])
        }
    else:
        return{
            'comment': "Unknown Error While Processing Request!",
            'result': 400,
            'reason': str(DrawMoneyCheck['reason'])
        }
print(DrawMoney("999", 200))