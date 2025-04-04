class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gp, sp = 0, 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0
        while gp < len(g) and sp < len(s):
            if g[gp] <= s[sp]:
                sp += 1
                gp += 1
                res += 1
            else:
                gp += 1

        return res