class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 
        results = [[]]
        for num in nums:
            results += [curr+[num] for curr in results]
            # 1st loop:
            #   results += [[1]]
            # 2nd:
            #   results += [[2], [1,2]]
            # 3rd:
            #   results += [[3],[2,3],[1,3],[1,2,3]]
        return results