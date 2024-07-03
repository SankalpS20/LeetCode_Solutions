class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                if num in rows[i] or num in columns[j] or num in boxes[(i // 3) * 3 + j // 3]:
                    return False
                
                rows[i][num] = rows[i].get(num, 0) + 1
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[(i // 3) * 3 + j // 3][num] = boxes[(i // 3) * 3 + j // 3].get(num, 0) + 1
        
        return True