class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, curr in enumerate(intervals):
            if curr[1] < newInterval[0]:
                res.append(curr)
            elif curr[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else: # curr intersect with new
                newInterval[0] = min(curr[0], newInterval[0])
                newInterval[1] = max(curr[1], newInterval[1])
        res.append(newInterval)
        return res