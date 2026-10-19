class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = 0
        n = len(nums)
        for i in range(n+1):
            target ^= i
        
        for num in nums:
            target ^= num
        
        return target