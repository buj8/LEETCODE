class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left, mostreps, maxlen = 0, 0, 0

        for right, char in enumerate(s):
            count[char] += 1
            mostreps = max(mostreps, count[char])
            while right - left >= mostreps + k:
                count[s[left]] -= 1
                left += 1
            maxlen = max(maxlen, right - left + 1)

        return maxlen