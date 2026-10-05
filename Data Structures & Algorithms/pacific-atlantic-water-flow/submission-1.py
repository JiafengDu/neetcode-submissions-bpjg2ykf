class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pac_q, atl_q = deque(), deque()
        pac, atl = set(), set()

        for c in range(cols):
            pac_q.append((0, c))
            pac.add((0, c))
            atl_q.append((rows-1, c))
            atl.add((rows-1, c))

        for r in range(rows):
            pac_q.append((r, 0))
            pac.add((r, 0))
            atl_q.append((r, cols-1))
            atl.add((r, cols-1))
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def bfs(queue: deque, visited: set):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        bfs(pac_q, pac)
        bfs(atl_q, atl)
        return [list(coord) for coord in pac & atl]
            
