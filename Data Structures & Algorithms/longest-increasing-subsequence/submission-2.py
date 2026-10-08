class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bisect_left(tails, num) -> int:
            left, right = 0, len(tails)
            while left < right:
                mid = left + (right-left)//2
                if tails[mid] >= num:
                    right = mid
                else:
                    left = mid+1
            return left
        tails = []

        for num in nums:
            idx = bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)