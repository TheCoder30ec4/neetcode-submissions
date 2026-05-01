class Solution:
    def arrangeCoins(self, n: int) -> int:

        
        num_coins =0

        while n>=num_coins:

            n = n-num_coins
            num_coins +=1

        return num_coins-1
        
            


        