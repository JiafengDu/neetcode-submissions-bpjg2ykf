class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0] if stones else 0
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x==y:
                continue
            else:
                heapq.heappush(stones, -abs(y-x))
        return -stones[0] if stones else 0