class Solution:
    def scoreOfString(self, s: str) -> int:

        i = 0
        j = 1
        total_sum = 0

        while j < len(s):

            difference = abs(ord(s[i]) - ord(s[j]))
            total_sum += difference
            i +=1
            j +=1

        return total_sum


        