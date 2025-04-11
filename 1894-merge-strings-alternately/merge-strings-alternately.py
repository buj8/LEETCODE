class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen = min(len(word1), len(word2))
        res = ""
        for i in range(minlen):
            res += word1[i] + word2[i]
        if len(word1) == len(word2):
            return res
        if len(word1) > len(word2):
            return res + word1[i+1:]
        return res + word2[i+1:]
        