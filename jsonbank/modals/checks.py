import json
from .pricepool import PricePool
# Limits
MaxLowerLimitVaule=0
# PATHS:
BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"

class Check:
    """
    This is a Python class named "Check". It has several methods that perform various functions related to bank transactions.

    The methods include:

    - AccountExistence
        - To check if the account exists in the bank.
    
    - Balance
        - To get the balance of a particular account.
    
    - SummedBalance
        - To get the sum of all balances of all accounts.
    
    - IfNegetive
        - To check if a certain amount can be drawn from an account without going below 0.
    
    - AddChecks
        - To add money to an account, and check if it exceeds the price pool limit.
    
    - DrawChecks
        - To draw money from an account, after checking if it will go below 0.
    
    The class uses the JSON file "BANK" as a source of data and makes changes to it as necessary.
"""
    def AccountExistence(AccountID:str):
        """
        This function is used to check if an account exists or not.
    
        Parameters:
            AccountID (str): The ID of the account to check.
        
        Returns:
            dict: A dictionary with the following keys:
                - comment (str): A string that describes if the account exists or not.
                -result (str): A string with value 'Pass' if the account exists, 'Fail' otherwise.
            
        Example:
            >>> AccountExistence('ABC123') -> 
                {'comment': 'Account Does exist!', 'result': 'Pass'}
            >>> AccountExistence('DEF456') -> 
                {'comment': 'Account Does not exist!', 'result': 'Fail'}
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
        This function takes AccountID as input and returns the balance in the specified account if the account exists.
    
        Parameters:
        AccountID (str): The account number for which the balance is to be retrieved.
    
        Returns:
        dict: A dictionary with two keys. The 'balance' key returns the balance of the specified account. 
        The 'result' key returns either 'Pass' if the account is found and balance is retrieved successfully 
        or 'Fail' if the account is not found.
    
        Example:
        >>> Balance("12345")
        {'balance': 5000, 'result': 'Pass'}
    
        >>> Balance("56789")
        {'comment': 'Account Not Found !', 'result': 'Fail'}
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
        SummedBalance() returns a dictionary object containing the sum of all accounts' balances in the bank and the result of the operation.
    
        Returns:
        >>> {'balance': int, 'result': 'Pass'}: A dictionary object with the following keys:
                - balance (int): The sum of all balances in the bank.
                - result (str): The result of the operation, either 'Pass' or 'Fail'.
                     In this case, it will always be 'Pass' as the function does not contain any conditions to return 'Fail'.
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
        This function checks if the account can be debited or not. 
    
        Parameters:
        AccountID (str): The account id of the user.
        Amount (int): The amount to be debited.
    
        Returns:
        dict: A dictionary containing the result of the check and a comment.
    
        Example:
        >>> IfNegetive(AccountID='123456', Amount=1000)
        {'comment': 'Amount Can be further drawn from this account !', 'result': 'Pass'}
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
        This function checks if an account exists and if there is enough money in the price pool to add a specified amount.
    
        Parameters:
        
        AccountID (str): The ID of the account to check for existence.
        
        AmountToAdd (int): The amount of money to add to the account.
    
        Returns:
        
        dict: A dictionary with two keys: "comment" and "result".
        
        - If the account exists, "comment" is either:
        
            - "Money Can Be Added !" if there is enough money in the price pool.
        
            - "Limit Exceeds Price Pool !" if the specified amount is greater than the balance in the price pool.
        
            - "Money can't be Added. Price Pool Turns 0" if the balance in the price pool is 0.
        
            - "An error occured." if something unexpected happens.
        
        
        - If the account does not exist, "comment" is "Account Not Found !".
        
        
        - In both cases, "result" is either "Pass" or "Fail", depending on whether the check passed or failed.
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
        Function to check if an amount of money can be withdrawn from a certain account.
    
        Parameters:
            AccountID (str): Account ID of the account from where the money is to be withdrawn.
            AmountToDraw (int): The amount of money that needs to be withdrawn.
        
        Returns:
            dict: A dictionary containing the result of the check, reason for the result and a comment on the check.
            The dictionary has the following keys:
                result (str): Result of the check, either 'Pass' or 'Fail'.
                reason (str): Reason for the result.
                comment (str): Comment on the result.
            
        The function performs the following checks:
        ```python
            1. Check the existence of the account from where the money is to be withdrawn using the Check.AccountExistence() function.
            2. If the account exists, it then checks if the withdrawal will result in a negative balance using the Check.IfNegetive() function.
            3. If the withdrawal does not result in a negative balance, the function returns 'Pass' and the reason and comment on the check.
            4. If the account does not exist, the function returns 'Fail' and the reason and comment on the check.
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
        The function takes 3 parameters:
        fromID: str : The Account ID from which the money will be transferred.
        toID: str : The Account ID to which the money will be transferred.
        Amount: int : The amount of money to be transferred.

        The function returns a dictionary object with 3 keys:
        
        
        ```python
        'comment': str : A message summarizing the outcome of the transfer.
        'reason': str : A detailed message explaining the reason behind the outcome of the transfer.
        'result': str : The result of the transfer. It can be either 'Pass' or 'Fail'.
        ```
        
        
        The function performs the following checks:
        
        
        ```json
        1. Check if the 'fromID' account exists in the database.
        2. If the 'fromID' account exists, check if the 'toID' account exists in the database.
        3. If both 'fromID' and 'toID' exists, check if the money can be transferred from the 'fromID' account (by calling Check.DrawChecks()).
        4. If the money can be transferred from the 'fromID' account, check if the money can be added to the 'toID' account (by calling Check.AddChecks()).
        5. Return the outcome of the transfer with a 'comment' and 'reason' message.
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
                            'reason': "Transfer Protocol Passed all the possible checks !",
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
        This function is used to check if the balance of an account can be added to the total balance flowing in the database.
        This function takes an input "Amount" which is the balance that is intended to be added.
    
        The function first retrieves the total balance flowing in the database using the "Check.SummedBalance()" method.
        This method returns a dictionary which includes the current balance flowing in the database.
    
        The "PricePool.check()" method is then used to retrieve the price pool balance.
        The price pool balance is stored in a dictionary, which is obtained from the "PricePool.check()" method.
    
        The difference between the current balance flowing in the database and the intended balance to be added is then calculated and stored in a variable called "CheckingAmount".
    
        If the value of "CheckingAmount" is greater than 0, then the balance can be added.
        The function returns a dictionary with the key-value pair {"comment": "Balance Can Be Added !", "result": "Pass"} in this case.
    
        If the value of "CheckingAmount" is less than 0, then the balance can't be added as it exceeds the price pool.
        The function returns a dictionary with the key-value pair {"comment": "New Balance Limit Exceeds Price Pool !", "result": "Fail"} in this case.
    
        If the value of "CheckingAmount" is equal to 0, then the balance can't be added as it will turn the price pool to 0.
        The function returns a dictionary with the key-value pair {"comment": "Balance can't be Added. Price Pool Turns 0", "result": "Fail"} in this case.
    
        In case of any error, the function returns a dictionary with the key-value pair {"comment": "An error occured.", 'result': "Error"}.
    
        :param Amount: An integer representing the balance intended to be added to the total balance flowing in the database.
        :return: A dictionary containing the comment, result and the reason for the result.
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