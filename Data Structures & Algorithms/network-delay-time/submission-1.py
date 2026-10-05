class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n+1)
        dist[k] = 0

        for _ in range(n-1):
            updated = False
            for u, v, w in times:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u]+w
                    updated = True
            if not updated:
                break
        
        max_time = max(dist[1:])
        return max_time if max_time != float("inf") else -1