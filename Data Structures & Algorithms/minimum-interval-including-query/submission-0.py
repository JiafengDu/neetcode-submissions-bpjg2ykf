class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res = {}
        i = 0
        n = len(intervals)

        for q in sorted(set(queries)):
            while i < n and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right-left+1, right))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            res[q] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]