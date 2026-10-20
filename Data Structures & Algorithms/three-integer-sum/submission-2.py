class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def helper(start: int, target: int, k: int) -> List[List[int]]:
            res = []
            n = len(nums)
            if start > n-k:
                return res
            
            if nums[start]*k > target or nums[-1]*k < target:
                return res
            
            if k == 2:
                left, right = start, n-1
                while left < right:
                    curr_sum = nums[left] + nums[right]
                    if curr_sum < target:
                        left += 1
                    elif curr_sum > target:
                        right -= 1
                    else:
                        res.append([nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left]==nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                return res
            for i in range(start, n-k+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                sub_results = helper(i+1, target-nums[i], k-1)
                for sub in sub_results:
                    res.append([nums[i]]+sub)
            return res
        return helper(0, 0, 3)