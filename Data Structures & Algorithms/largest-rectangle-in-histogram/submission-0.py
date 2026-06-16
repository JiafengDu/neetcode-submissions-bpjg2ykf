class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # loop over heights
        # assume new start is now
        # while last of stack height > h:
        #   old rec must stop now, pop and update max_area
        #   start for the current should be from prev index
        # stack should append current (start, h)
        # after running through all heights:
        # stack has heights from small to big
        # we calculate the area of each from start to end of list
        
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i-index))
                start = index
            
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h*(len(heights)-i))
        
        return max_area