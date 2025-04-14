class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        n_islands = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # Seen/out of bounds/0 -> ignore it
            if (
                (r, c) in seen or
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"
            ):
                return
            
            seen.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == "1":
                    dfs(r, c)
                    n_islands += 1
            
        return n_islands