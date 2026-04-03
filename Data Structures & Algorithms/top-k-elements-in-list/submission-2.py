class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        frequencies = [[] for _ in range(n+1)]
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            frequencies[c].append(n)

        res = []
        for i in range(len(frequencies)-1, 0, -1):
            for n in frequencies[i]:
                res.append(n)
                if len(res) == k:
                    return res