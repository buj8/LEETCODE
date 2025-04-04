class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0 
        skill.sort()

        l, r = 0, len(skill)-1

        target = skill[l] + skill[r]

        while l < r:
            current = skill[l] + skill[r]
            if target == current:
                res += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1

        return res