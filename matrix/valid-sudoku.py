class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count=0
       
        rows=len(board)
        cols=len(board[0])
        boxes = defaultdict(set)
        seen={}
        row_seen = [set() for _ in range(rows)]
        col_seen = [set() for _ in range(cols)]
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in row_seen[row] or board[row][col] in col_seen[col] or board[row][col] in boxes[(row // 3, col // 3)]:
                    return False
                row_seen[row].add(col)
                col_seen[col].add(row)
                boxes[(row // 3, col // 3)].add(board[row][col])
        

    
        return True