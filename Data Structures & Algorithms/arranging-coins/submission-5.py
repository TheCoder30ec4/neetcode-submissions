class Solution:
    def arrangeCoins(self, n: int) -> int:

        left,right = 1,n

        max_rows = 0

        while left<=right:

            mid = (left+right)//2
            num_coins = (mid/2)*(mid+1)

            if num_coins>n:
                right = mid-1
            else:
                left = mid+1
                max_rows = max(mid,max_rows)


        return max_rows

        