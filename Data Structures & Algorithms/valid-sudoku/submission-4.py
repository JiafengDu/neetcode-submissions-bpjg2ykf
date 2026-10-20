class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                digit = board[r][c]
                if digit in rows[r] or digit in cols[c] or digit in boxes[r//3][c//3]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[r//3][c//3].add(digit)
        
        return True
                