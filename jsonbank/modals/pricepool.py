import json

MaxLowerLimitVaule=0
# PATHS:
BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"



class PricePool:
    """
    The following code implements a class PricePool that interacts with a JSON file "pricepool.json" located in the directory "./banking/". The class has three methods - `check()`, `add()`, and `reset()` - that allow checking the balance of the pool, adding an amount to the pool, and resetting the pool to zero respectively.
    """
    def check():
        """
        Returns a dictionary containing the current balance of the price pool.
        
        Returns:
            dict: A dictionary with the following keys:
                - balance (int): The current balance of the price pool.
        """
        with open(POOLING, "r") as file:
            Pool = json.load(file)
        return {
            "balance": Pool["maximum"]
        }
        
            
    def add(AmountToAdd:int=None):
        """
        Adds a specified amount to the price pool.
        
        Args:
            AmountToAdd (int, optional): The amount to add to the pool. Defaults to None.
        
        Returns:
            dict: A dictionary with the following keys:
                - comment (str): A string indicating the success or failure of the addition.
                - result (int): An integer indicating the status code (200 for success, 400 for failure).
        
        Note:
            If `AmountToAdd` is None, the method returns a dictionary indicating that no amount was requested to add to the pool.
        """
        with open(POOLING, "r") as file:
            if AmountToAdd==None:
                return {
                    "comment":"No amount requested to add to the Price Pool. Check Again.",
                    'result':400
                }
            else:
                Pool = json.load(file)
                ExistingPool=Pool["maximum"]
                NewPool=ExistingPool+AmountToAdd
                Pool["maximum"] = NewPool
                with open(POOLING, "w") as file:
                    json.dump(Pool, file, indent=2)
                LatestPool=Pool["maximum"]       
                return {
                    "comment":f"Price Pool updated. Current Price Pool is: {LatestPool}",
                    'result':200
                }
    def sub(AmountToSub:int=None):
        """
        Subtracts a specified amount from the price pool.
        
        Args:
            AmountToSub (int, optional): The amount to subtract from the pool. Defaults to None.
        
        Returns:
            dict: A dictionary with the following keys:
                - comment (str): A string indicating the success or failure of the subtraction.
                - result (int): An integer indicating the status code (200 for success, 400 for failure).
        
        Note:
            If `AmountToSub` is None, the method returns a dictionary indicating that no amount was requested to subtract from the pool.
        """
        with open(POOLING, "r") as file:
            if AmountToSub==None:
                return {
                    "comment":"No amount requested to subtract to the Price Pool. Check Again.",
                    'result':400
                }
            else:
                Pool = json.load(file)
                ExistingPool=Pool["maximum"]
                NewPool=ExistingPool-AmountToSub
                Pool["maximum"] = NewPool
                with open(POOLING, "w") as file:
                    json.dump(Pool, file, indent=2)
                LatestPool=Pool["maximum"]       
                return {
                    "comment":f"Price Pool updated. Current Price Pool is: {LatestPool}",
                    'result':200
                }
    def reset():
        """
        Resets the price pool to zero.
        
        Returns:
            dict: A dictionary with the following keys:
                - now (int): The current balance of the pool (i.e., 0).
                - was (int): The previous balance of the pool.
                - result (int): An integer indicating the status code (200 for success).
        """
        with open(POOLING, "r") as file:
                Pool = json.load(file)
                ExistingPool=Pool["maximum"]
                ZeroPool=ExistingPool-ExistingPool
                Pool["maximum"] = ZeroPool
                with open(POOLING, "w") as file:
                    json.dump(Pool, file, indent=2)
                LatestPool=Pool["maximum"]
                return {
                "now":LatestPool, 
                "was": ExistingPool, 
                "result":200
                }
