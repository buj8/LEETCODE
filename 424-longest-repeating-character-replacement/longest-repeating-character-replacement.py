from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s):
            return len(s)
        
        counter = Counter()
        counter[s[0]] = 1
        
        l, r = 0, 1
        maxlen = 1  # Initialize to 1 since we start with one character
        
        while l < r and r < len(s):
            # Add the new character to our counter
            counter[s[r]] += 1
            
            # Get the most frequent character count in current window
            max_char_count = counter.most_common(1)[0][1]
            
            # If current window size - most frequent character count > k,
            # we need more than k replacements, so shrink the window
            if (r - l + 1) - max_char_count > k:
                counter[s[l]] -= 1
                l += 1
            else:
                # Update max length if current window is larger
                maxlen = max(maxlen, r - l + 1)
            
            r += 1
        
        return maxlen