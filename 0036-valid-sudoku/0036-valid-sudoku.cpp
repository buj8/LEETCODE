class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<char>> rows(9);
        vector<set<char>> columns(9);
        vector<set<char>> boxes(9);

        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                char number = board[i][j];
                if(number != '.') {
                    int box_id = (i / 3) * 3 + j / 3;
                    
                    if(rows[i].find(number) != rows[i].end() || 
                        columns[j].find(number) != columns[j].end() ||
                        boxes[box_id].find(number) != boxes[box_id].end()) {
                            return false;
                        }
                    rows[i].insert(number);
                    columns[j].insert(number);
                    boxes[box_id].insert(number);
                }
            }
        }

        return true;
    }
};