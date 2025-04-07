class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        h, w = len(grid), len(grid[0])
        seen = set()
        n_islands = 0

        def getNeighbors(r, c):
            neighbors = []
            candidates = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for candidate in candidates:
                if (
                    candidate[0] >= 0 and candidate[0] < h
                    and candidate[1] >= 0 and candidate[1] < w
                    and grid[candidate[0]][candidate[1]] == '1' 
                ):
                    neighbors.append(candidate)
            return neighbors

        def bfs(sr, sc):
            queue = [(sr, sc)]
            while len(queue) > 0:
                r, c = queue.pop(0)  
                if (r, c) not in seen:                  
                    seen.add((r, c))
                    for neighbor in getNeighbors(r, c):
                        queue.append(neighbor)


        for i, row in enumerate(grid):
            for j, square in enumerate(row):
                if square == '1' and (i, j) not in seen:
                    bfs(i, j)
                    n_islands += 1

        return n_islands


    