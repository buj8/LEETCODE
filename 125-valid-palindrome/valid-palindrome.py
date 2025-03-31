class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = ""
        for char in s:
            if char.isalnum():
                s2 += char
        l, r = 0, len(s2)-1
        print(s2)
        while l < r:
            if s2[l] != s2[r]:
                return False
            l += 1
            r -= 1
        
        return True