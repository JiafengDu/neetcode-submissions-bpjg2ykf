class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            visited = set()
            for s in board[x]:
                if s!='.' and s in visited:
                    return False
                else:
                    visited.add(s)
        for y in range(9):
            visited = set()
            for x in range(9):
                piece = board[x][y]
                if piece!='.' and piece in visited:
                    return False
                else:
                    visited.add(piece)

        for x in range(1,4):
            for y in range(1,4):
                visited = set()
                for i in range(3*x-3, 3*x):
                    for j in range(3*y-3, 3*y):
                        piece = board[i][j]
                        if piece!='.' and piece in visited:
                            return False
                        else:
                            visited.add(piece)
        
        return True