class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums = 1,3,4,2,2
        # detect cycle
        #   slow=fast=0
        #   move slow by 1 step (nums[slow])
        #   move fast by 2 (nums[nums[fast]])
        #   until slow == fast
        # find cycle entrance
        #   slow2 = 0
        #   advance both slow and slow2
        #   until slow==slow2
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
