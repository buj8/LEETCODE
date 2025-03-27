class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        l, r = 0, 1
        maxlen = 0

        seen = {s[0] : 0}

        while l < r and r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                maxlen = max(maxlen, r - l)
                l = seen[s[r]] + 1
            seen[s[r]] = r 
            r += 1    
            
        return max(maxlen, r - l)