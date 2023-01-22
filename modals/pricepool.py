import json

MaxLowerLimitVaule=0
# PATHS:
BANK="./banking/bank.json"
POOLING="./banking/pricepool.json"



class PricePool:
    def check():
        
        """_summary_
        To check the latest PricePool !
        Returns:
            _type_: _description_
        
        Source Reference:
        ```python
        with open(POOLING, "r") as file:
            Pool = json.load(file)
        return {
            "balance": Pool["maximum"]
        }```
        """
        
        
        with open(POOLING, "r") as file:
            Pool = json.load(file)
        return {
            "balance": Pool["maximum"]
        }
        
            
    def add(AmountToAdd:int=None):
        
        
        """_summary_
            Adds the amount to Price Pool for extending the Maximum Money Floating Limit of the Bank!
        Args:
            AmountToAdd (int, optional): _description_. Integer Value of the Amount that has to be added.
        Sources:
        ```python
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
                }```
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
    def add(AmountToSub:int=None):
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
        """_summary_
        Resets the whole pricepool! 

        Source:
        ```python
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
                }```
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
