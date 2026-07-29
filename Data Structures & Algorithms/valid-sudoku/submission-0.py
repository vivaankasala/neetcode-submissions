class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        square={}
        row={}
        col={}

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if c not in col:
                    col[c]=set()
                if r not in row:
                    row[r]=set()
                
                box_key=(r//3,c//3)
                if box_key not in square:
                    square[box_key]=set()
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False
                if board[r][c] in square[box_key]:
                    return False


                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[box_key].add(board[r][c])

        return True