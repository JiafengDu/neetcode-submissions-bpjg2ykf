class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_count = 0

        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        iteration = 0
        while queue and fresh_count!=0:
            for _ in range(len(queue)):
                rot_m, rot_n = queue.popleft()
                for delta_m, delta_n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nei_m = rot_m+delta_m
                    nei_n = rot_n+delta_n
                    if nei_m>=0 and nei_m<m and nei_n>=0 and nei_n<n and grid[nei_m][nei_n] == 1:
                        grid[nei_m][nei_n] = 2
                        queue.append((nei_m, nei_n))
                        fresh_count -= 1
            iteration += 1
        
        return iteration if fresh_count==0 else -1
        

