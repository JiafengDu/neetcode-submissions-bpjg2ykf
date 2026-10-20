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
        idx = n
        while len(res)<k:
            if buckets[idx]:
                while buckets[idx]:
                    res.append(buckets[idx].pop())
                    if len(res)==k:
                        return res
            idx -= 1
        return res

