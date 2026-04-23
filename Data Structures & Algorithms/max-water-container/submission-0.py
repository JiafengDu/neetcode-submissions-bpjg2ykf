class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0

        while l<r:
            if heights[l] <= heights[r]:
                shortest = heights[l]
                l += 1
            else:
                shortest = heights[r]
                r -= 1
            res = max(res, shortest * (r-l+1))
        return res