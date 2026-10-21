class Solution:
    def trap(self, height: List[int]) -> int:
        # water level at i = min(max_left, max_right)
        # trapped at i = max(0, level[i] - height[i])
        # [2,1,9]
        if not height:
            return 0
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        total_water = 0
        while left < right:
            if max_left<max_right:
                left += 1
                max_left = max(max_left, height[left])
                total_water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                total_water += max_right - height[right]
        return total_water