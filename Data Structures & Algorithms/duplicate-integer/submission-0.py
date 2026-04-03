class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        return len(setNums)!=len(nums)