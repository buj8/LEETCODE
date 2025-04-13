class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(curr, i, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i == len(candidates):
                return

            # Case 1: We add another copy of the number
            curr.append(candidates[i])
            dfs(curr, i, total + candidates[i])

            # Case 2: We try with the next
            curr.pop()
            dfs(curr, i+1, total)

        dfs([], 0, 0)
        return res