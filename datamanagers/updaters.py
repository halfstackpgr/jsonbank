import json
import sys
sys.setrecursionlimit(1000)

MaxLowerLimitVaule=0
# PATHS:

BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"

class Update:
    def addmoney(AccountID:str, AmountToAdd:int):
    
    
        """
        Source Code:
        
        ```python
        with open(BANK, "r") as file:
            thebank = json.load(file)
        ExistingBalace=thebank[str(AccountID)][0]["Balance"]
        NewAmount=AmountToAdd+ExistingBalace
        thebank[str(AccountID)][0]["Balance"] = NewAmount   
        with open(BANK, "w") as file:
            json.dump(thebank, file, indent=2)
        return {
            "was": ExistingBalace,
            "now": NewAmount,
            "result": 200
        }
        ```
        
        """
        with open(BANK, "r") as file:
            thebank = json.load(file)
        ExistingBalace=thebank[str(AccountID)][0]["Balance"]
        NewAmount=AmountToAdd+ExistingBalace
        thebank[(AccountID)][0]["Balance"] = NewAmount   
        with open(BANK, "w") as file:
            json.dump(thebank, file, indent=2)
        return {
            "was": ExistingBalace,
            "now": NewAmount,
            "result": 200
        }
    def drawmoney(AccountID:str, AmountToWithDraw:int):
        
        
        """
        Source Code:
        
        ```python
        with open(BANK, "r") as file:
            thebank = json.load(file)
            ExistingBalace=thebank[str(AccountID)][0]["Balance"]
            NewAmount=ExistingBalace-AmountToWithdraw
            thebank[str(AccountID)][0]["Balance"] = NewAmount
            with open(BANK, "w") as file:
                json.dump(thebank, file, indent=2)
            return {
                "was": ExistingBalace,
                "now": NewAmount,
                "result": 200
            }    
        ```
        
        """
        with open(BANK, "r") as file:
            thebank = json.load(file)
            ExistingBalace=thebank[str(AccountID)][0]["Balance"]
            NewAmount=ExistingBalace-AmountToWithDraw
            thebank[(AccountID)][0]["Balance"] = NewAmount
            with open(BANK, "w") as file:
                json.dump(thebank, file, indent=2)
            return {
                "was": ExistingBalace,
                "now": NewAmount,
                "result": 200
            }
    def transfer(fromID:str, toID:str, Amount:int):
        
        
        """
        Source Code:
        
        ```python
        Update.drawmoney(AccountID=fromID, AmountToWithdraw=Amount)
        Update.addmoney(AccountID=toID, AmountToAdd=Amount)
        return {
            'comment':f'Trasnfer of {Amount} from the ID {fromID} to the ID {toID}, was sucessfull !',
            'result': 200
        }
        ```
        
        """
        Update.drawmoney(AccountID=fromID, AmountToWithDraw=Amount)
        Update.addmoney(AccountID=toID, AmountToAdd=Amount)
        return {
            'comment':f'Trasnfer of {Amount} from the ID {fromID} to the ID {toID}, was sucessfull !',
            'result': 200
        }

class UpdateUser:
    def name(AccountID:str, NewName:str):
        with open(BANK, "r") as file:
            thebank = json.load(file)
            WasName= thebank[str(AccountID)][0]["AccountName"]
            thebank[str(AccountID)][0]["AccountName"] = str(NewName)
            with open(BANK, "w") as file:
                json.dump(thebank, file, indent=2)
            return {
                "was": str(WasName).title(),
                "now": str(NewName).title(),
                "result": 200
            }
    def branchname(AccountID:str, NewBranch:str):
        with open(BANK, "r") as file:
            thebank = json.load(file)
            WasName= thebank[(AccountID)][0]["BranchName"]
            thebank[str(AccountID)][0]["BranchName"] = str(NewBranch)
            with open(BANK, "w") as file:
                json.dump(thebank, file, indent=2)
            return {
                "was": str(WasName).title(),
                "now": str(NewBranch).title(),
                "result": 200
            }  
    def branchid(AccountID:str, NewBranchID:int):
        with open(BANK, "r") as file:
            thebank = json.load(file)
            WasID= thebank[(AccountID)][0]["BranchID"]
            thebank[(AccountID)][0]["BranchID"] = NewBranchID
            with open(BANK, "w") as file:
                json.dump(thebank, file, indent=2)
            return {
                "was": WasID,
                "now": NewBranchID,
                "result": 200
            }

    def about(AccountID:str, NewAbout:str):
        with open(BANK, "r") as file:
            thebank = json.load(file)
            WasAbout= thebank[str(AccountID)][0]["About"]
            thebank[str(AccountID)][0]["About"] = NewAbout
            with open(BANK, "w") as file:
                json.dump(thebank, file, indent=2)
            return {
                "was": WasAbout,
                "now": NewAbout,
                "result": 200
            }
