import json
import sys
sys.setrecursionlimit(1000)

MaxLowerLimitVaule=0
# PATHS:

BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"

class Update:
    
    
    
    """
    Update is a class that contains methods for updating bank account information in a json file.

    Methods:
    
    - addmoney(AccountID:str, AmountToAdd:int) -> dict:
    Given an account ID and an amount to add, this method will add the amount to the existing balance of the account in the json file and return a dictionary with the existing balance, new balance, and result code.
    
    - drawmoney(AccountID:str, AmountToWithDraw:int) -> dict:
    Given an account ID and an amount to withdraw, this method will subtract the amount from the existing balance of the account in the json file and return a dictionary with the existing balance, new balance, and result code.
    
    - transfer(fromID:str, toID:str, Amount:int) -> dict:
    Given two account IDs and an amount to transfer, this method will withdraw the amount from the first account and add it to the second account in the json file. It will return a dictionary with a comment and result code.
    """
    def addmoney(AccountID:str, AmountToAdd:int):
        """
        Add money to an account.
        Parameters:
        AccountID (str): The ID of the account to add money to.
        AmountToAdd (int): The amount of money to add to the account.
    
        Returns:
        dict:
        ```json
            {
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
        Withdraw money from an account.
    
        Parameters:
        AccountID (str): The ID of the account to withdraw money from.
        AmountToWithDraw (int): The amount of money to withdraw from the account.
    
        Returns:
        dict:
        ```json
            {
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
        Transfer money from one account to another.
    
        Parameters:
        fromID (str): The ID of the account to transfer money from.
        toID (str): The ID of the account to transfer money to.
        Amount (int): The amount of money to transfer.
    
        Returns:
        dict:
        ```json
            {
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
    """
    This class contains various functions to update and delete account information in a BANK json file.

    Functions:
    - name(AccountID:str, NewName:str): Takes in an AccountID and a new Name as input and updates the Account Name in the BANK json file.
    - branchname(AccountID:str, NewBranch:str): Takes in an AccountID and a new Branch Name as input and updates the Branch Name in the BANK json file.
    - branchid(AccountID:str, NewBranchID:int): Takes in an AccountID and new BranchID as parameter and updates the corresponding account's BranchID in the bank file.
    - about(AccountID:str, NewAbout:str): Takes in an AccountID and new About as parameter and updates the corresponding account's about in the bank.
    - deleteAccount(AccountID:str): Takes in an AccountID as a parameter and deletes the corresponding account from the bank.
    """
    def name(AccountID:str, NewName:str):
        """
        This function takes in an AccountID and a new Name as input and updates the Account Name in the BANK json file.
    
        Parameters:
        - AccountID (str): The ID of the account whose Name is to be updated.
        - NewName (str): The new Account Name.
    
        Returns:
        A dictionary containing the old Account Name, new Account Name and a result code.
        {
            "was": "Old Account Name",
            "now": "New Account Name",
            "result": 200
        } 
        """
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
        
        """
        This function takes in an AccountID and a new Branch Name as input and updates the Branch Name in the BANK json file.
    
        Parameters:
        - AccountID (str): The ID of the account whose Branch Name is to be updated.
        - NewBranch (str): The new Branch Name.
    
        Returns:
        A dictionary containing the old Branch Name, new Branch Name and a result code.
        ```json
        {
            "was": "Old Branch Name",
            "now": "New Branch Name",
            "result": 200
        }
        ```
        """
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
        """
        This function takes in an AccountID and new BranchID as parameter and updates the corresponding account's BranchID in the bank file.
    
        Parameters:
            AccountID (str): The ID of the account whose BranchID is to be updated.
            NewBranchID (str) : The new BranchID of the account.
        
        Returns:
            dict : A dictionary containing the previous BranchID, the new BranchID and the result code (200) if the BranchID has been updated successfully.
        """
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
        """
        This function takes in an AccountID and new About as parameter and updates the corresponding account's about in the bank.

        Parameters:
            AccountID (str): The ID of the account whose about is to be updated.
            NewAbout (str) : The new about of the account.
        
        Returns:
            dict : A dictionary containing the previous about, the new about and the result code (200) if the about has been updated successfully.
        """
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
    def deleteAccount(AccountID:str):
        """
        This function takes in an AccountID as a parameter and deletes the corresponding account from the bank.
        
        Parameters:
            AccountID (str): The ID of the account to be deleted.
        
        Returns:
            dict : A dictionary containing the result code (200) and a comment "Account has been deleted successfully !" if the account has been deleted.
        """
        with open(BANK, "r") as file:
            thebank = json.load(file)
            thebank.pop(AccountID, None)
            with open(BANK, "w") as file:
                json.dump(thebank, file, indent=2)
            return {
                "result": 200,
                "comment": "Account has been deleted successfully !"
            }
    
    
class UpdateBank:   
    def pool(NewAmount:int):
        with open(POOLING, "r") as file:
            POOLINGDATA = json.load(file)
            POOLINGDATA["maximum"] = NewAmount
            with open(POOLING, "w") as file:
                json.dump(POOLINGDATA, file, indent=2)
            return {
                "result": 200,
                "comment": f"New Amount Of {NewAmount} has been added to the bank!"
            }