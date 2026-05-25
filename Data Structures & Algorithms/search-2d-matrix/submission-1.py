class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:



        def BinarySearch(nums: List[int], target:int):

            l,r = 0, len(nums)-1 

            while l<=r:
                mid = (l+r)//2 

                if nums[mid] == target:
                    return True 
                elif nums[mid] < target:
                    l = mid+1 
                else:
                    r = mid-1

            return False

            
        
        for i in range(len(matrix)):

            if matrix[i][-1] >= target:

                return BinarySearch(matrix[i], target)
        return False
