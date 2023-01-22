import json
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
        thebank[str(AccountID)][0]["Balance"] = NewAmount   
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
            thebank[str(AccountID)][0]["Balance"] = NewAmount
            with open(BANK, "w") as file:
                json.dump(thebank, file, indent=2)
            return {
                "was": ExistingBalace,
                "now": NewAmount,
                "result": 200
            }
    def transfer(fromID:str, toID:str, Amount):
        
        
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
        Update.drawmoney(AccountID=fromID, AmountToWithdraw=Amount)
        Update.addmoney(AccountID=toID, AmountToAdd=Amount)
        return {
            'comment':f'Trasnfer of {Amount} from the ID {fromID} to the ID {toID}, was sucessfull !',
            'result': 200
        }






