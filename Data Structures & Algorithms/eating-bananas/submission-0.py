class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k=1,2,3,4,5,6,7
        def calcTime(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)
            return time

        l = 1
        r = max(piles)
        res = r
        while l<=r:
            mid = l + (r-l)//2
            if calcTime(mid) <= h:
                res = mid
                r = mid-1
            elif calcTime(mid) > h:
                l = mid+1
        return res

