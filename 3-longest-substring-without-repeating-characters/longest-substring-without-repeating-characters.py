class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        n = len(s)

        if n < 2:
            return n

        start, currlen, maxlen = 0, 0, 0

        for end in range(n):
            if s[end] in seen and seen[s[end]] >= start:
                start = seen[s[end]]+1
                currlen = 1
            seen[s[end]] = end
            currlen = end-start+1
            maxlen = max(maxlen, currlen)
        
        
        return maxlen