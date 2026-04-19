class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current = 1
        prefix = []
        for num in nums:
            prefix.append(current)
            current *= num
        
        current = 1
        suffix = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = current
            current *= nums[i]

        result = [prefix[i]*suffix[i] for i in range(len(nums))]
        return result