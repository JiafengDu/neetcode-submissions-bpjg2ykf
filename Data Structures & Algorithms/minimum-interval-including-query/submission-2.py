class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        coords = sorted(set(x for l, r in intervals for x in (l, r, r+1)))
        k = len(coords)

        rank = {val: i for i, val in enumerate(coords)}

        INF = float("inf")
        tree = [INF] * (2*k)
        def update(l_idx: int, r_idx: int, val: int) -> None:
            l_idx += k
            r_idx += k
            while l_idx <= r_idx:
                if l_idx % 2 == 1:
                    if val < tree[l_idx]:
                        tree[l_idx] = val
                    l_idx += 1
                if r_idx % 2 == 0:
                    if val < tree[r_idx]:
                        tree[r_idx] = val
                    r_idx -= 1
                
                l_idx //= 2
                r_idx //= 2
        
        def query(idx: int) -> int:
            idx += k
            res = INF
            while idx > 0:
                if tree[idx] < res:
                    res = tree[idx]
                idx //=2
            return res if res != INF else -1
        
        def bisect_right(arr: List[int], target: int) -> int:
            l, r = 0, len(arr)
            while l<r:
                mid = (l+r)//2
                if arr[mid] <= target:
                    l = mid + 1
                else: # arr[mid] bigger than target
                    r = mid
            return l

        for left, right in intervals:
            size = right-left+1
            update(rank[left], rank[right], size)
        
        ans = []
        for q in queries:
            idx = bisect_right(coords, q)-1
            if idx < 0:
                ans.append(-1)
            else:
                ans.append(query(idx))
        
        return ans
