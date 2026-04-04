class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = -1001
        subarray = 0
        for num in nums:
            subarray += num
            largest = max(largest, subarray)

            if subarray < 0:
                subarray = 0
        return largest