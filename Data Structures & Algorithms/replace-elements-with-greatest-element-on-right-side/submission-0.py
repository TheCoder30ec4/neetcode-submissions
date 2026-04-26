class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)-1):

            if i+1 >= len(arr)-1:
                arr[i] = arr[len(arr)-1]
            else:
                arr[i] = max(arr[(i+1):len(arr)])

        if len(arr) > 0:
            arr[len(arr)-1] = -1

        return arr