class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        list_of_letters = s.split()

        return len(list_of_letters[-1:][0])
        