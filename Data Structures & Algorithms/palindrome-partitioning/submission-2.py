class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[] for _ in range(len(s)+1)]
        dp[0] = [[]]

        for end in range(1, len(s)+1):
            for start in range(end):
                sub = s[start:end]
                if sub == sub[::-1]:
                    for prev_partition in dp[start]:
                        dp[end].append(prev_partition+[sub])
        return dp[len(s)]