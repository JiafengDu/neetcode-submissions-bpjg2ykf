class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort first
        # at each step, choose an element starting from curr idx
        # if current element is less than target, and the remaining target is more or equal to current element, we can pick
        # if remaining reach 0, current path is valid
        # if remaining is less than current element, prune that branch
        nums.sort()
        res = []
        def backtrack(start: int, comb: List[int], remain: int):
            if remain == 0:
                res.append(comb.copy())
                return
            
            for i in range(start,len(nums)):
                if nums[i] > remain:
                    break
                comb.append(nums[i])
                backtrack(i, comb, remain-nums[i])
                comb.pop()
        
        backtrack(0, [], target)
        return res