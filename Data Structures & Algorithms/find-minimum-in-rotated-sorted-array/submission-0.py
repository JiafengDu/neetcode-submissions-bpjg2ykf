class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        # if we found the smallest element, it should be smaller than all other ele
        # first choose left, right, then calc mid, mid compare with left, right
        # [2,3,1]
        # if mid > right, cont. to consider only mid to right
        # [1,2,3]
        # if mid < right, cont. to consider only left to mid
        # [3,4,5,1,2]
        # mid is 5, 5 > 2, cont. to consider [5,1,2]
        # 1 is < 2, cont. to consider [1]
        # since left==right, return
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            
        return nums[left]
            