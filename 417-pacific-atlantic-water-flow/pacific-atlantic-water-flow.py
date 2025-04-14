class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev):
            if (
                (r, c) in visited or
                r < 0 or r >= len(heights) or
                c < 0 or c >= len(heights[0]) or
                heights[r][c] < prev
            ):
                return
            
            visited.add((r, c))

            curr = heights[r][c]

            dfs(r + 1, c, visited, curr)
            dfs(r - 1, c, visited, curr)
            dfs(r, c + 1, visited, curr)
            dfs(r, c - 1, visited, curr)


        rows = len(heights)
        cols = len(heights[0])

        for i in range(rows):
            dfs(i, 0, pacific, -float('inf'))
            dfs(i, cols-1, atlantic, -float('inf'))

        for i in range(cols):
            dfs(0, i, pacific, -float('inf'))
            dfs(rows-1, i, atlantic, -float('inf'))

        return list(atlantic & pacific)
