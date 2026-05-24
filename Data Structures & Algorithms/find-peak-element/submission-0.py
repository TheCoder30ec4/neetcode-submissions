class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        

        largest_num = nums[0]
        index = 0

        for i in range(1,len(nums)):

            if largest_num < nums[i]:
                largest_num = nums[i]
                index = i

        
        return index