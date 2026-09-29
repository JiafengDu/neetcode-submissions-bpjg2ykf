class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # choose 1/2/3
        # for 1 path, choose 2/3
        # for 2 path, only choice is 3
        def dfs(perm, subList: List[int]):
            if len(subList)==0:
                res.append(perm.copy())
                return

            for i in range(len(subList)):
                perm.append(subList[i])
                dfs(perm, subList[:i]+subList[i+1:])
                perm.pop()
        dfs([], nums)
        return res
        

            


        