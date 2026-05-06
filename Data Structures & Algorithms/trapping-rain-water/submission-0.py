class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total_water = 0

        for current_index, current_height in enumerate(height):
            while stack and current_height > height[stack[-1]]:
                bottom_index = stack.pop()

                if not stack:
                    break
                left_index = stack[-1]
                width = current_index - left_index - 1
                bounded_height = min(current_height, height[left_index]) - height[bottom_index]

                total_water += width * bounded_height

            stack.append(current_index)
        return total_water