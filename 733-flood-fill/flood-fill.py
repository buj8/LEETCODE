class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        h, w = len(image), len(image[0])
        
        visited = set()
        queue = [(sr, sc)]
        base_color = image[sr][sc]

        if base_color == color:
            return image

        def neighbors(r, c):
            candidates = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            res = []
            for candidate in candidates:
                if (
                    candidate[0] >= 0 and candidate[0] < h 
                    and candidate[1] >= 0 and candidate[1] < w
                    and image[candidate[0]][candidate[1]] == base_color 
                ):
                    res.append(candidate)
            return res

        while len(queue) > 0:
            # queue.pop(0) -> BFS
            # queue.pop() -> DFS
            r, c = queue.pop(0)
            if (r, c) not in visited:
                visited.add((r, c))
                image[r][c] = color
                for neighbor in neighbors(r, c):
                    queue.append(neighbor)

        return image
        
