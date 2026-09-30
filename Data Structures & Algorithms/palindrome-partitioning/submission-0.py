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
        def is_palindrome(sub: str) -> bool:
            left, right = 0, len(sub)-1
            while left < right:
                if sub[left]==sub[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        def dfs(start:int):
            if start==len(s):
                res.append(curr.copy())
            for end in range(start, n):
                if is_palindrome(s[start:end+1]):
                    curr.append(s[start:end+1])
                    dfs(end+1)
                    curr.pop()
        
        dfs(0)
        return res