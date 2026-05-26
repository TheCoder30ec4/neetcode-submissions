class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        i, j = 0, 0
        res = ''
        while i < len1 and j < len2:
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        if i < len1:
            res += word1[i:]
        if j < len2:
            res += word2[j:]
        return res
