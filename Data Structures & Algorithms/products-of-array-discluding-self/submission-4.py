class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [1]*n
        suf_prod = [1]*n

        prod = 1
        for i in range(1, n):
            prod *= nums[i-1]
            pre_prod[i] = prod
        
        prod = 1
        for i in range(n-2, -1, -1):
            prod *= nums[i+1]
            suf_prod[i] = prod

        res = [1]*n
        for i in range(n):
            res[i] = pre_prod[i]*suf_prod[i]
        
        return res
