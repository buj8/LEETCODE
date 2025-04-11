class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        # Pre-allocate list with the exact size needed
        chars = [''] * (n1 + n2)
        
        # Fill the list with alternating characters
        for i in range(min(n1, n2)):
            chars[i*2] = word1[i]
            chars[i*2+1] = word2[i]
        
        # Add remaining characters from the longer word
        if n1 > n2:
            for i in range(n2, n1):
                chars[n2*2 + (i-n2)] = word1[i]
        else:
            for i in range(n1, n2):
                chars[n1*2 + (i-n1)] = word2[i]
        
        return ''.join(chars)