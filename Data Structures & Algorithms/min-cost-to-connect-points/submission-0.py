class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0,0)] # (cost, point_index)
        total_cost = 0

        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)

            if u in visited:
                continue
            
            visited.add(u)
            total_cost += cost

            x1, y1 = points[u]
            for v in range(n):
                if v not in visited:
                    dist = abs(x1-points[v][0]) + abs(y1-points[v][1])
                    heapq.heappush(min_heap, (dist, v))
        return total_cost