class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        def rec(i, currList):
            if i == len(nums):
                results.append(currList[:])
                return

            currList.append(nums[i])
            rec(i+1, currList)
            
            currList.pop()
            rec(i+1, currList)
            
        rec(0, [])
        return results