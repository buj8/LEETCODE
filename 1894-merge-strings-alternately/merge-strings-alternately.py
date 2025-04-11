class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        minlen = min(n1, n2)
        res = ""
        for i in range(minlen):
            res += word1[i] + word2[i]
        if len(word1) == len(word2):
            return res
        if len(word1) > len(word2):
            return res + word1[n2:]
        return res + word2[n1:]
        