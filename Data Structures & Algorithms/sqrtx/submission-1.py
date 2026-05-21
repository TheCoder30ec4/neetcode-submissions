class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0

        neartest = 1 

        left = 1 

        right = x 

        while left <= right:

            mid = (left+right)//2 

            squared = mid *mid 

            if squared > x:
                right = mid-1 
            elif squared < x and squared > neartest:
                neartest = mid 
                left = mid +1 
            elif squared == x:
                return mid 
            
        return neartest

        