class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # matrix[0][?] -> matrix[?][2]
        # matrix[r][?] -> matrix[?][n-1-r]
        # matrix[?][0] -> matrix[0][?]
        # matrix[?][c] -> matrix[c][?]

        # so we can first:
        #   matrix[r][c] -> matrix[n-1-r][c] (reverse rows)
        # then:
        #   matrix[n-1-r][c] -> matrix[c][n-1-r] (transpose)
        n = len(matrix)
        matrix.reverse()
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        