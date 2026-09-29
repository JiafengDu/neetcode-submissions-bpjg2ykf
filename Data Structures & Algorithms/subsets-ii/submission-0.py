class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # for eacch element, append it to existing subsets. 
        # if nums[i] == nums[i-1], only append nums[i] to subsets that were created during the immediately preceding iteration.
        res = [[]]
        nums.sort()
        end_idx = 1
        for i in range(len(nums)):
            prec_idx = 0
            if i>0 and nums[i] == nums[i-1]:
                prec_idx = end_idx
            end_idx = len(res)
            for j in range(prec_idx, end_idx):
                res.append(res[j]+[nums[i]])
        return res