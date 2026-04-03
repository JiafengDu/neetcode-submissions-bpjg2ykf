class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, num in enumerate(nums):
            other = target - num
            if other not in mem:
                mem[num] = i
            else:
                return [mem[other], i]