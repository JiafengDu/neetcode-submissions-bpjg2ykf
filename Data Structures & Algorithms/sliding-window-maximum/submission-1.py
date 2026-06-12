class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1,2,1,0,4,2,6
        # consider ex. 6,2,3,1,1,6 and k=3
        # 
        # answer is 6,3,3,6
        # brute force approach:
        # 
        res = []
        curr_max = max(nums[:k])
        res.append(curr_max)
        for i in range(k, len(nums)): 
            curr_max = max(nums[i-k+1:i+1])
            res.append(curr_max)
        return res
