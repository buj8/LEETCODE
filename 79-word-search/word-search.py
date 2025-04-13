class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # Optimize: If the word is longer than the board can possibly hold
        if len(word) > rows * cols:
            return False
        
        # Count characters in the word and board to enable early pruning
        word_counts = Counter(word)
        board_counts = Counter(char for row in board for char in row)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
        
        def dfs(row, col, index, visited):
            # Base case: reached the end of the word
            if index == len(word):
                return True
                
            # Check bounds and if the current cell matches the next character
            if (row < 0 or row >= rows or col < 0 or col >= cols or 
                (row, col) in visited or board[row][col] != word[index]):
                return False
            
            # Mark as visited
            visited.add((row, col))
            
            # Check all four directions
            result = (dfs(row + 1, col, index + 1, visited) or
                    dfs(row - 1, col, index + 1, visited) or
                    dfs(row, col + 1, index + 1, visited) or
                    dfs(row, col - 1, index + 1, visited))
            
            # Backtrack by removing from visited
            visited.remove((row, col))
            
            return result
        
        # Try starting from each cell
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0, set()):
                    return True
        
        return False