class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [defaultdict(bool) for _ in range(9)]
        cols = [defaultdict(bool) for _ in range(9)]
        boxes= [defaultdict(bool) for _ in range(9)]

        for row_id in range(9):
            for col_id in range(9):
                num = board[row_id][col_id]
                if num != ".":
                    box_id = math.floor(row_id/3)*3 + math.floor(col_id/3)
                    if rows[row_id][num] or cols[col_id][num] or boxes[box_id][num]:
                        return False
                    rows[row_id][num], cols[col_id][num], boxes[box_id][num] = True, True, True
        
        return True

                    