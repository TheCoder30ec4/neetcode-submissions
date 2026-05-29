class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        res = set()

        for i in range(len(words)):
            for j in range(len(words)):

                if i == j:
                    continue

                if words[i] in words[j]:
                    res.add(words[i])
                elif words[j] in words[i]:
                    res.add(words[j])
                else:
                    continue
        return list(res)