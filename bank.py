import json

from .datamanagers.get import UserGet, BankGet
from .datamanagers.converters import Converters, AllResults
from .datamanagers.updaters import Update, UpdateUser
from .modals.checks import Check
from .modals.pricepool import PricePool
import sys
sys.setrecursionlimit(1000)

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
    """
    Source:
    
    ```python
    CreateAccount(AccountID:str, AccountName:str, BranchName:str, BranchID:int, Balance:int, About:str) -> dict
    ```
    This function creates a new account in the bank with the given parameters.

    Parameters:
    
    - AccountID (str): The ID of the account.
    
    - AccountName (str): The name of the account holder.
    
    - BranchName (str): The name of the branch where the account is created.
    
    - BranchID (int): The ID of the branch where the account is created.
    
    - Balance (int): The initial balance of the account.
    
    - About (str): Additional information about the account.

    Returns:
    
    - dict: A dictionary with a 'result' key (int) indicating the status of the operation and a 'comment' key (str) providing more information about the operation.

"""
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
    """
    Source: 
    ```python
    AddMoney(AccountID:str, Amount:int) -> dict
    ```
    This function is used to add money to a given account.

    The function first performs a check using `Check.AddChecks(AccountID, AmountToAdd)` to verify that the add operation is valid. If the check passes, the function calls `Update.addmoney(AccountID, AmountToAdd)` to add the money to the account.

    The function returns a dictionary with keys 'comment', 'result', and 'reason'. The 'comment' key holds a string describing the outcome of the operation, the 'result' key holds an integer indicating the status of the operation, and the 'reason' key holds a string with the reason for the outcome.
    
    Either `200` for success or `400` for failure.
    """
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
    """
    Source:
    
    ```python
    DrawMoney(AccountID:str, Amount:int) -> dict
    ```
    
    This function is used to withdraw money from a given account.

    The function first performs a check using Check.DrawChecks(AccountID, AmountToDraw) to verify that the withdraw operation is valid. If the check passes, the function calls Update.drawmoney(AccountID, AmountToWithDraw) to withdraw the money from the account.

    The function returns a dictionary with keys 'comment', 'result', and 'reason'. The 'comment' key holds a string describing the outcome of the operation, the 'result' key holds an integer indicating the status of the operation, and the 'reason' key holds a string with the reason for the outcome.
    
    Either `200` for success or `400` for failure.
    """
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
def Transfer(fromID:str, toID:str, Amount:int):
    """
    Source:
    
    ```python
    Transfer(fromID:str, toID:str, Amount:int)->dict
    ```
    
    This function is used to transfer money from one account to another account.

    The function first performs a check using Check.TransferCheck(fromID, toID, Amount) to verify that the transfer operation is valid. If the check passes, the function calls Update.transfer(fromID, toID, Amount) to transfer the money.

    The function returns a dictionary with keys 'comment', 'result', and 'reason'. The 'comment' key holds a string describing the outcome of the operation, the 'result' key holds an integer indicating the status of the operation, and the 'reason' key holds a string with the reason for the outcome.
    
    Either `200` for success or `400` for failure.
    """
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
        """
        This method returns the balance of an account, along with the balance in words and a comment.
        
        Parameters:
            AccountID (str): The ID of the account for which the balance is to be retrieved.
        
        Returns:
            dict: A dictionary containing the following keys:
                - balance: The balance of the account in standard format.
                - balanceInWords: The balance of the account in words.
                - comment: A comment on the balance retrieval.
                - result: 200 if the balance was retrieved successfully, 400 if the account was not found.
        """
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
        """
        This method returns the name of an account, along with a comment.
        
        Parameters:
            AccountID (str): The ID of the account for which the name is to be retrieved.
        
        Returns:
            dict: A dictionary containing the following keys:
                - name: The name of the account.
                - comment: A comment on the name retrieval.
                - result: 200 if the name was retrieved successfully, 400 if the account was not found.
        """
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
        """
        This method returns the branch name of an account, along with a comment.
        
        Parameters:
            AccountID (str): The ID of the account for which the branch name is to be retrieved.
        
        Returns:
            dict: A dictionary containing the following keys:
                - branchname: The name of the branch associated with the account.
                - comment: A comment on the branch name retrieval.
                - result: 200 if the branch name was retrieved successfully, 400 if the account was not found.
        """
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
        """
        This method returns the Branch ID of the account holder.
        
        Parameters:
            AccountID (str): Account ID of the account holder.
            
        Returns:
            dict: containing Branch ID, comment and result code.
            {
                'branchid': int,
                'comment': str,
                'result': int
            }
            - result: 200 if the branch ID was retrieved successfully, 400 if the account was not found.
        """
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
        """
        This function gets the user's details from the UserGet.About() method, which returns the about field of the user's account.
        If the account exists, it returns the about field in title case, a comment about the about field, and a status code `200`.
        If the account does not exist, it returns a status code `400` and a comment about the account not being found.
        
        Parameters:
            AccountID (str): The ID of the user's account
        
        Returns:
            dict: A dictionary containing the about field in title case, the comment, and the status code.
            
        ```json
            {
                'about': str(AboutUser).title(),
                'comment': f"About: {AboutUser}",
                'result': 200
            }
        ```
        """
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
        """
        This function retrieves all the details of the user's account by calling the other functions in this class (name, branchid, branchname, AboutUser).
        If the account exists, it returns a dictionary with all the fields of the user's account, a status code `200` and a comment about the successful retrieval of the details.
        If the account does not exist, it returns a status code `400` and a comment about the account not being found.
        
        Parameters:
            AccountID (int): The ID of the user's account
        
        Returns:
            dict: A dictionary containing all the fields of the user's account, the status code and the comment.
        ```json
            {
                'name':Name,
                'a/cid':ACID,
                'branchid':BranchID,
                'branchname':BranchName,
                'about':AboutTheUser,
                'result': 200,
                'comment': "Bank Got The Details Successfullly!"
            }
        ```
        """
        CheckAccount=Check.AccountExistence(AccountID=AccountID)
        if CheckAccount['result']=='Pass':
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
                'about':AboutTheUser,
                'result': 200,
                'comment': "Bank Got The Details Successfullly!"
            }
        if CheckAccount['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }
class GetBank:
    """
    A class for retrieving various information from a bank.
    This class contains four methods:
    - SumOfBalance(): retrieves the total balance in the bank and returns it in both standard format and in words.
    - NumOfAccounts(): retrieves the total number of accounts in the bank and returns it in both standard format and in words.
    - Pool(): retrieves the maximum amount that can flow into accounts and returns it in both standard format and in words.
    - RemainingPool(): retrieves the remaining pool in the bank and returns it in both standard format and in words.
    """
    def SumOfBalace():
        """
        This method is used to fetch the sum of the balance in all the accounts in the bank.
        It calls the `BankGet.Balance()` method which returns a dictionary with the key 'balance'
        The returned 'balance' value is then passed to `Converters.StandardFormat(int(SumUp))` to get the standard format of the balance.
        Then the same balance value is passed to `Converters.NumberToWords(int(SumUp))` to get the balance value in words.

        Returns:
            A dictionary containing the following keys:
                - balance: (int) The net balance flowing in the bank in standard format.
                - balanceinwords: (str) The net balance flowing in the bank in words.
                - comment: (str) A comment on the balance value.
                - result: (int) 200 if the request was successful.
        """
        SumUp=BankGet.Balance()['balance']
        return{
            'balance': Converters.StandardFormat(int(SumUp)),
            'balanceinwords': Converters.NumberToWords(int(SumUp)),
            "comment":f"The Net Balance flowing in the bank is: {Converters.NumberToWords(int(SumUp))}",
            "result": 200
        }
    def NumOfAccounts():
        """
        Method that returns the number of accounts in the bank.
        
        Returns:
            dict: 
                - 'accounts': The number of accounts in the bank in standard format.
                - 'accountsinwords': The number of accounts in the bank in words.
                - 'comment': A string indicating the total number of accounts in the bank.
                - 'result': 200 if successful.
        """
        Num=BankGet.Accounts()['accounts']
        return{
            'accounts': Converters.StandardFormat(int(Num)),
            'accountsinwords': Converters.NumberToWords(int(Num)),
            "comment":f"The Total Number Of Accounts in the bank are: {Converters.NumberToWords(int(Num))}",
            "result": 200
        }
    def Pool():
        """
        Returns the maximum amount that can flow into accounts

        Returns:
            dict: {
                'maxpool': (str) The maximum amount in standard format,
                'maxpoolinwords': (str) The maximum amount in words,
                'comment': (str) A comment describing the returned value,
                'result': (int) A code indicating the success of the operation (200 for success)
            }
        """
        PoolNum=BankGet.Pool()['balance']
        return{
            'maxpool': Converters.StandardFormat(int(PoolNum)),
            'maxpoolinwords': Converters.NumberToWords(int(PoolNum)),
            "comment":f"The maximum amount that can flow into accounts: {Converters.NumberToWords(int(PoolNum))}",
            "result": 200
        }
    def RemainingPool():
        """
        This function returns the remaining pool of funds in the bank as of now.
        Returns:
            dict : containing the remaining pool of funds in standard format, in words, a comment and a result code.
                {
                    'remainingpool': <remaining pool in standard format>,
                    'remainingpoolinwords': <remaining pool in words>,
                    'comment': <Comment on the remaining pool>,
                    'result': <result code>
                }
        """
        RemainingPool=BankGet.RemainingPool()['leftpool']
        return{
            'maxpool': Converters.StandardFormat(int(RemainingPool)),
            'maxpoolinwords': Converters.NumberToWords(int(RemainingPool)),
            "comment":f"The maximum amount that can flow into accounts as of now : {Converters.NumberToWords(int(RemainingPool))}",
            "result": 200
        } 

class ChangeUser:
    def name(AccountID:str, NewName:str):
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck['result']=='Pass':
            Change=UpdateUser.name(AccountID=AccountID, NewName=NewName)
            return {
                'was': str(Change['was']).title(),
                'new': str(Change['now'].title()),
                'result': 200,
                'comment':'Request was sucessfull'
                
            }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }
    def branchname(AccountID:str, NewBranch:str):
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck['result']=='Pass':
            Change=UpdateUser.branchname(AccountID=AccountID, NewBranch=NewBranch)
            return {
                'was': str(Change['was']).title(),
                'new': str(Change['now'].title()),
                'result': 200,
                'comment':'Request was sucessfull',
            }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }
    def branchid(AccountID:str, NewBranchID:str):
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck['result']=='Pass':
            Change=UpdateUser.branchid(AccountID=AccountID, NewBranchID=NewBranchID)
            return {
                'was': Change['was'],
                'new': Change['now'],
                'result': 200,
                'comment':'Request was sucessfull'
            }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }
    def about(AccountID:str, NewAbout:str):
        AccountExistenceCheck=Check.AccountExistence(AccountID=AccountID)
        if AccountExistenceCheck['result']=='Pass':
            Change=UpdateUser.about(AccountID=AccountID, NewAbout=NewAbout)
            return {
                'was': str(Change['was']).title(),
                'new': str(Change['now'].title()),
                'result': 200,
                'comment':'Request was sucessfull'
            }
        if AccountExistenceCheck['result']=='Fail':
            return{
                'result':400,
                'comment':'Account Not Found!'
            }