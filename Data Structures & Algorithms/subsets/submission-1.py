class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for num in nums:
            results += [curr+[num] for curr in results]
        return results