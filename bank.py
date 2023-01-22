import json
import datamanagers.converters
import datamanagers.updaters
import datamanagers.get
import modals.pricepool
import modals.checks
from datamanagers.get import UserGet, BankGet
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
                    "BranchName": BranchName,
                    "BranchID": BranchID,
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
            'comment': "Amount Could Not Be Drawn from the account!",
            'result': 400,
            'reason': str(DrawMoneyCheck['reason'])
        }
    else:
        return{
            'comment': "Unknown Error While Processing Request!",
            'result': 400,
            'reason': str(DrawMoneyCheck['reason'])
        }
<<<<<<< HEAD
def Transfer(fromID:str, toID:str, Amount:int):
    TransferCheck=Check.TransferCheck(fromID=fromID, toID=toID, Amount=Amount)
    if TransferCheck['result']=='Pass':
        Update.transfer(fromID=fromID, toID=toID, Amount=Amount)
        return{
            'comment': "Amount has been successfully transferred !",
            'result': 200,
            'reason': str(TransferCheck['reason'])
        }
    if TransferCheck['result']=='Fail':
        return{
            'comment': "Amount Could Not Be transfered from the account!",
            'result': 400,
            'reason': str(TransferCheck['reason'])
        }
    else:
        return{
            'comment': "Unknown Error While Processing Request!",
            'result': 400,
            'reason': str(TransferCheck['reason'])
        }

class GetUser:
    def balance(AccountID:str):
        CheckAccount=Check.AccountExistence(AccountID=AccountID)
        if CheckAccount['result']=='Pass':
            balance=UserGet.UserBalance(AccountID=AccountID)["balance"]
            return{
                'balance': Converters.StandardFormat(balance),
                'balanceInWords': Converters.NumberToWords(balance),
                'comment': f"The Balance for the account {AccountID} is {balance}",
                'result': 200
            }
        if CheckAccount['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }
    def name(AccountID:str):
        CheckAccount=Check.AccountExistence(AccountID=AccountID)
        if CheckAccount['result']=='Pass':
            NameUser=UserGet.AccountName(AccountID=AccountID)["name"]
            return{
                'name': str(NameUser).title(),
                'comment': f"The name for the account {AccountID} is {NameUser}",
                'result': 200
            }
        if CheckAccount['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }

    def branchname(AccountID:str):
        CheckAccount=Check.AccountExistence(AccountID=AccountID)
        if CheckAccount['result']=='Pass':
            NameBranch=UserGet.BranchName(AccountID=AccountID)["branchname"]
            return{
                'branchname': str(NameBranch).title(),
                'comment': f"The Branch Name for the account {AccountID} is {NameBranch}",
                'result': 200
            }
        if CheckAccount['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }
    def branchid(AccountID:str):
        CheckAccount=Check.AccountExistence(AccountID=AccountID)
        if CheckAccount['result']=='Pass':
            IDBranch=UserGet.BranchID(AccountID=AccountID)["branchid"]
            return{
                'branchid': int(IDBranch),
                'comment': f"The Branch ID for the account {AccountID} is {IDBranch}",
                'result': 200
            }
        if CheckAccount['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }
    def AboutUser(AccountID:str):
        CheckAccount=Check.AccountExistence(AccountID=AccountID)
        if CheckAccount['result']=='Pass':
            AboutUser=UserGet.About(AccountID=AccountID)["about"]
            return{
                'about': str(AboutUser).title(),
                'comment': f"About: {AboutUser}",
                'result': 200
            }
        if CheckAccount['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }
    def all(AccountID:int):
        Name=GetUser.name(AccountID=AccountID)['name']
        ACID=AccountID
        BranchID=GetUser.branchid(AccountID=AccountID)['branchid']
        BranchName=GetUser.branchname(AccountID=AccountID)['branchname']
        AboutTheUser=GetUser.AboutUser(AccountID=AccountID)['about'].title()
        return{
            'name':Name,
            'a/cid':ACID,
            'branchid':BranchID,
            'branchname':BranchName,
            'about':AboutTheUser
        }
=======
>>>>>>> 70b47a5eb7f27d48a8c19483569faf4ba502f9a9
