class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count=0
       
        rows=len(board)
        cols=len(board[0])
        seen={}
        row_seen = [set() for _ in range(rows)]
        col_seen = [set() for _ in range(cols)]
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in row_seen[row] or board[row][col] in col_seen[col]:
                    return False
                row_seen[row].add(col)
                col_seen[col].add(row)
    
        return True