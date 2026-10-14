class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[1]-x[0])
        sorted_queries = sorted(set(queries))
        m = len(sorted_queries)

        parent = list(range(m+1))

        def find(i: int) -> int:
            path = []
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for node in path:
                parent[node] = i
            return i
        
        def bisect_left(arr: List[int], target: int) -> int:
            l, r = 0, len(arr)
            while l < r:
                mid = (l+r)//2
                if arr[mid] < target:
                    l = mid + 1
                else: # arr[mid] >= target (mid could be the leftmost)
                    r = mid
            return l

        res = {}

        for left, right in intervals:
            size = right-left+1
            idx = find(bisect_left(sorted_queries, left))
            while idx < m and sorted_queries[idx] <= right:
                res[sorted_queries[idx]] = size
                parent[idx] = find(idx+1)
                idx = parent[idx]
            
        return [res.get(q, -1) for q in queries]