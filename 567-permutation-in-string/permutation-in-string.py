class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d=Counter(s1)
        for i in range(0,len(s2)-len(s1)+1):
            a=Counter(s2[i:i+len(s1)])
            if a==d:
                return True
        return False