class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def recursion(i, target, current):
            if target == 0:
                results.append(current[:])
                return
            if i == len(candidates):
                return
            
            if candidates[i] <= target:
                current.append(candidates[i])
                recursion(i+1, target-candidates[i], current)
                current.pop()
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            recursion(i+1, target, current)
        
        recursion(0, target, [])
        return results