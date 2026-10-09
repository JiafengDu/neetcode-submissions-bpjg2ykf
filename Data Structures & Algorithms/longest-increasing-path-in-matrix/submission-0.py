class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(r: int, c: int) -> int:
            if (r, c) in dp:
                return dp[(r,c)]
            
            res = 1

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc]>matrix[r][c]:
                    res = max(res, 1+dfs(nr, nc))
            
            dp[(r,c)] = res
            return res
        
        max_path = 0
        for r in range(rows):
            for c in range(cols):
                max_path = max(max_path, dfs(r, c))
        return max_path
            
            