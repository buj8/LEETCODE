class Solution:
    def longestPalindrome(self, s: str) -> str:        
        res = ""

        def getMax(l, r):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    longest = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
            return s[l+1:r]
        
        for i in range(len(s)):
            odd = getMax(i, i)
            even = getMax(i, i+1)
            candidate = odd if len(odd) > len(even) else even
            res = candidate if len(candidate) > len(res) else res

        return res
