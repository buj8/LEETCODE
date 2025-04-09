class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r  = 0, len(s1)-1
        needed = Counter(s1)
        remaining = len(s1)

        if len(s1) > len(s2):
            return False

        # we initialize the first window
        for i in range(len(s1)):
            if s2[i] in needed:
                needed[s2[i]] -=1
                if needed[s2[i]] >= 0:
                    remaining -=1
        
        if remaining == 0:
            return True

        while r < len(s2)-1:
            if s2[l] in needed:
                needed[s2[l]] +=1
                if needed[s2[l]] > 0:
                    remaining +=1
            l += 1
            r += 1
            if s2[r] in needed:
                needed[s2[r]] -=1
                if needed[s2[r]] >= 0:
                    remaining -=1
            
            #print(s2[l:r+1])
            #print(remaining)
            if remaining == 0:
                return True

        return False