class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start: int, comb: List[int], target):
            if target == 0:
                res.append(comb.copy())
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtrack(i+1, comb, target-candidates[i])
                comb.pop()
        
        backtrack(0, [], target)
        return res
                