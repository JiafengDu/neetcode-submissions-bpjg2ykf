class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        for row in range(m):
            seen = set()
            for i in range(n):
                if board[row][i] == '.': continue
                if board[row][i] not in seen:
                    seen.add(board[row][i])
                else:
                    return False
        

        for col in range(n):
            seen = set()
            for i in range(m):
                if board[i][col] == '.': continue
                if board[i][col] not in seen:
                    seen.add(board[i][col])
                else:
                    return False
        
        for i in range(0, m, 3):
            for j in range(0, n, 3):
                seen = set()
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if board[x][y] == '.': continue
                        if board[x][y] not in seen:
                            seen.add(board[x][y])
                        else:
                            return False
        return True
        