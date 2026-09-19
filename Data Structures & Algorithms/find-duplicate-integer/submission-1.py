class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            target = nums[0]
            nums[0], nums[target] = nums[target], nums[0]
        
        return nums[0]
