class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rowSet = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in rowSet:
                    return False
                rowSet.add(board[row][i])
        
        for col in range(9):
            colSet = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in colSet:
                    return False
                colSet.add(board[i][col])
        
        for square in range(9):
            squareSet = set()
            #divide the 9 x 9 to 3 x 3, hence why you divide by 3 in this case, s that you iterate through the subsquares
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in squareSet:
                        return False
                    squareSet.add(board[row][col])
        return True