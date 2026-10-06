class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float("inf")]*n
        min_dist[0] = 0
        visited = [False]*n
        total_cost = 0

        for _ in range(n):
            curr_node = -1
            curr_min = float("inf")
            for i in range(n):
                if not visited[i] and min_dist[i] < curr_min:
                    curr_min = min_dist[i]
                    curr_node = i
            visited[curr_node] = True
            total_cost += curr_min

            x1, y1 = points[curr_node]
            for next_node in range(n):
                if not visited[next_node]:
                    dist = abs(x1-points[next_node][0])+abs(y1-points[next_node][1])
                    if dist < min_dist[next_node]:
                        min_dist[next_node] = dist
        return total_cost