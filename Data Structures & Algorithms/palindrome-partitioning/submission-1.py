class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # dfs(start_idx) exploring all possible partition cuts from start_idx to end
        # loop through every end idx end from start_idx to n-1.
        # if s[start_idx:end+1] is a palindrome, push it to the path list and recurse on dfs(end+1)
        # base: start_idx==len(s), create a copy of curr and add it to res
        # backtracking: pop the last added substring after returning from deeper recursion to explore alternate cuts
        res = []
        curr = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
        
        def dfs(start:int):
            if start==len(s):
                res.append(curr.copy())
                return
            for end in range(start, n):
                if dp[start][end]:
                    curr.append(s[start:end+1])
                    dfs(end+1)
                    curr.pop()
        
        dfs(0)
        return res