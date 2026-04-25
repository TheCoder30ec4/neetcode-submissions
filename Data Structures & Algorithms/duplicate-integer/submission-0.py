class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        pack = set()

        for i in nums:
            if i in pack:
                return True
            else:
                pack.add(i)

        return False