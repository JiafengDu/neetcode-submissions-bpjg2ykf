class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maximum = 0
        for num in nums_set:
            if num-1 not in nums_set:
                start, length = num, 0
                while start in nums_set:
                    length += 1
                    start += 1
                maximum = max(maximum, length)
        return maximum