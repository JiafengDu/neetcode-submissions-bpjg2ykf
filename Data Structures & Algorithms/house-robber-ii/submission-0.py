class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        rob1_h0, rob2_h0 = nums[0], max(nums[0], nums[1])
        for n in nums[2:-1]:
            rob1_h0, rob2_h0 = rob2_h0, max(n+rob1_h0, rob2_h0)
        
        rob1_skip, rob2_skip = 0, nums[1]
        for n in nums[2:]:
            rob1_skip, rob2_skip = rob2_skip, max(n+rob1_skip, rob2_skip)
        
        return max(rob2_h0, rob2_skip)