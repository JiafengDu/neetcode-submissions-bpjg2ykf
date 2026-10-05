class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(r: int, c: int, visited: set):
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]:
                    dfs(nr, nc, visited)
        
        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows-1, c, atl)
        
        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols-1, atl)
        
        return [list(coord) for coord in pac & atl]