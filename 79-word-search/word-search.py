class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def getNeighbors(x, y, seen):
            candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            neighbors = []
            for candidate in candidates:
                if (
                    candidate not in seen
                    and candidate[0] >= 0 and candidate[0] < len(board)
                    and candidate[1] >= 0 and candidate[1] < len(board[0])
                ):
                    neighbors.append(candidate)
            return neighbors
                    
        def dfs(x, y, i, seen):
            _seen = seen.copy()
            _seen.add((x,y))

            if board[x][y] != word[i]:
                return False

            if i == len(word) - 1:
                return True
            
            neighbors = getNeighbors(x, y, seen)

            if not neighbors:
                return False

            paths = []
            for n in neighbors:
                paths.append(dfs(n[0], n[1], i + 1, _seen))

            return any(paths)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True

        return False