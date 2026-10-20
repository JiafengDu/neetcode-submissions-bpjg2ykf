class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res)==k:
                    return res
                    
        return res

