class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        target = sum(skill) / (len(skill) / 2)

        available = defaultdict(int)
        
        skill.sort()

        for s in range(len(skill)//2, len(skill)):
            available[skill[s]] += 1
        

        for i in range(len(skill)//2):
            needed = target - skill[i]
            if needed in available:
                available[needed] -= 1
                if available[needed] == 0:
                    del available[needed]
                res += skill[i] * needed
            else:
                return -1

        return int(res) 