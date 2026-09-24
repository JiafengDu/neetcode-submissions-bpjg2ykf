class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = [0]*len(nums)
        product = 1
        
        for num in nums:
            pre.append(product)
            product *= num
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            suf[i] = product
            product *= nums[i]
        
        res = []
        for i, num in enumerate(nums):
            res.append(pre[i]*suf[i])
        
        return res