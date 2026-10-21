class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l to r
        # area = (r-l) * min(heights[l], heights[r])
        # first maximize width ->
        #   l, r = 0, n-1
        # [7,10,x,1,7] -> max is 30
        left, right = 0, len(heights)-1
        max_water = 0
        while left < right:
            width = right - left
            h_left = heights[left]
            h_right = heights[right]

            if h_left < h_right:
                area = width * h_left
                left += 1
            else:
                area = width * h_right
                right -= 1
            
            if area > max_water:
                max_water = area
        return max_water