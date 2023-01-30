import json

# To be only used by Bank Lib!
# Limits
MaxLowerLimitVaule=0
# PATHS:
BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"


class UserGet:
    """
    A class for retrieving information about a user's account in a bank.
    
    Methods:
        UserBalance(AccountID:str) -> Dict[str,int]: Returns the balance of the user's account
        AccountName(AccountID:str) -> Dict[str,str]: Returns the name of the user's account
        BranchName(AccountID:str) -> Dict[str,str]: Returns the name of the branch where the user's account is located
        BranchID(AccountID:str) -> Dict[str,int]: Returns the ID of the branch where the user's account is located
        About(AccountID:str) -> Dict[str,str]: Returns a brief description of the user's account
    """
    def UserBalance(AccountID:str):
        """
        This method returns the balance of the user with the provided Account ID.
        
        Parameters:
            AccountID (str): The ID of the user's account.
        
        Returns:
            dict: A dictionary containing the balance of the user, in the format {'balance': balance}.
        """
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'balance':int(thebank[AccountID][0]["Balance"])
        }
    def AccountName(AccountID:str):
        """
        This method returns the name of the user with the provided Account ID.
        
        Parameters:
            AccountID (str): The ID of the user's account.
        
        Returns:
            dict: A dictionary containing the name of the user, in the format {'name': name}.
        """
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'name':str(thebank[AccountID][0]["AccountName"])
        }
    def BranchName(AccountID:str):
        """
        This method returns the branch name of the user with the provided Account ID.
        
        Parameters:
            AccountID (str): The ID of the user's account.
        
        Returns:
            dict: A dictionary containing the branch name of the user, in the format {'branchname': branchname}.
        """
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'branchname':str(thebank[AccountID][0]["BranchName"])
        }
    def BranchID(AccountID:str):
        """
        This method returns the branch ID of the user with the provided Account ID.
        
        Parameters:
            AccountID (str): The ID of the user's account.
        
        Returns:
            dict: A dictionary containing the branch ID of the user, in the format {'branchid': branchid}.
        """
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'branchid':int(thebank[AccountID][0]["BranchID"])
        }     
    def About(AccountID:str):
        """
        This method returns the about of the user with the provided Account ID.
        
        Parameters:
            AccountID (str): The ID of the user's account.
        
        Returns:
            dict: A dictionary containing the about of the user, in the format {'about': about}.
        """
        with open(BANK, "r") as file:
            thebank = json.load(file)
        return{
            'about':str(thebank[AccountID][0]["About"])
        }

class BankGet:
    """
    A class for retrieving information about the bank.
    
    Methods:
        Balance() -> Dict[str,int]: Returns the total balance of all the accounts in the bank
        Accounts() -> Dict[str,int]: Returns the total number of accounts in the bank
        Pool() -> Dict[str,int]: Returns the maximum amount of money that can be stored in the bank
        RemainingPool() -> Dict[str,int]: Returns the remaining amount of money that can be stored in the bank
    """
    def Balance():
        """
        This method returns the total balance of all the accounts in the bank.
        
        Returns:
            dict: A dictionary containing the total balance of all accounts, in the format {'balance': balance}.
        """
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
        """
        This method returns the total number of accounts in the bank.
        
        Returns:
            dict: A dictionary containing the total number of accounts, in the format {'accounts': accounts}.
        """
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
        """
        This method returns the maximum pool available in the bank.
        
        Returns:
            dict: A dictionary containing the maximum pool available, in the format {'balance': balance}.
        """
        with open(POOLING, "r") as file:
            Pool = json.load(file)
        return {
            "balance": Pool["maximum"]
        }
    def RemainingPool():
        """
        This method returns the remaining pool available in the bank after deducting the used pool from the maximum pool.
        
        Returns:
            dict: A dictionary containing the remaining pool available, in the format {'leftpool': leftpool}.
        """
        PoolLatest=BankGet.Pool()['balance']
        UsedPool=BankGet.Balance()['balance']
        RemainingPool=PoolLatest-UsedPool
        return{
            'leftpool':RemainingPool
        }
