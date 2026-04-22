class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, 3, 0, 0)
    
    def kSum(self, nums, k, target, start):
        res = []

        if start == len(nums):
            return res

        average_value = target // k
        if nums[start] > average_value or nums[-1] < average_value:
            return res    

        if k==2:
            return self.twoSum(nums, target, start)

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue

            for subset in self.kSum(nums, k-1, target-nums[i], i+1):
                res.append([nums[i]]+subset)
        return res

    def twoSum(self, nums, target, start):
        res = []
        l, r = start, len(nums)-1
        while l<r:
            curr_sum = nums[l] + nums[r]
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1
        return res    