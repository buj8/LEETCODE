class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, left, res = defaultdict(int), 0, 0
        maxfreq = 0
        for right, curr_char in enumerate(s):
            count[curr_char] += 1
            maxfreq = max(maxfreq, count[curr_char])

            while right - left - maxfreq >= k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res