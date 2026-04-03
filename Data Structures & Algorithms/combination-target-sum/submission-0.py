class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(i, target, current):
            if target==0:
                results.append(current[:])
                return
            
            if i == len(nums):
                return
            
            if nums[i] <= target:
                current.append(nums[i])
                dfs(i, target-nums[i], current)
                current.pop()
        
            dfs(i+1, target, current)
        
        dfs(0, target, [])
        return results