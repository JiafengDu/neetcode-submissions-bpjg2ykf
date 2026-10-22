class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while mono and temperatures[mono[-1]] < temp:
                prev = mono.pop()
                res[prev] = i-prev
            mono.append(i)
        return res