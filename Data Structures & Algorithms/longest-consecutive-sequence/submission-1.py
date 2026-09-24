class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 100,4,200,1,3,2
        # convert to set
        # identify sequence starts
        # see 100, no 99, seq start, check 101, no->length=1
        # see 4, 3 in set, skip
        # 200, no 199, seq start, check 201, no->length=1
        # 1, no 0, seq start, check 2, yes, length+=1, 3yes, +=1, 4 yes, +=1
        # 3, 2 in set, skip
        # 2, 1 in set, skip
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:
                length = 1
                while (num+length) in num_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest