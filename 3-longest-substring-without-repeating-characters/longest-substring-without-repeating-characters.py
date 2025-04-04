class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        l, r = 0, 0
        seen = defaultdict(int)
        while r < len(s):
            if s[r] in seen:
                while l < seen[s[r]]:
                    del seen[s[l]]
                    l += 1
                l = seen[s[r]] + 1
                seen[s[r]] = r
            seen[s[r]] = r
            r += 1
            maxlen = max(maxlen, r-l)
        return maxlen