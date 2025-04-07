class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        h, w = len(grid), len(grid[0])
        seen = set()
        n_islands = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Definido una sola vez

        def bfs(sr, sc):
            queue = deque([(sr, sc)])
            seen.add((sr, sc))  # Marcar como visitado al agregar
            
            while queue:
                r, c = queue.popleft()  # O(1) en vez de O(n)
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < h and 0 <= nc < w and 
                        grid[nr][nc] == '1' and (nr, nc) not in seen):
                        queue.append((nr, nc))
                        seen.add((nr, nc))  # Marcar al agregar, no al procesar

        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1' and (i, j) not in seen:
                    bfs(i, j)
                    n_islands += 1

        return n_islands