class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        min_heap = [(0, k)]
        visited = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited[node] = time

            if len(visited) == n:
                return time
            
            for weight, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time+weight, neighbor))
        return -1