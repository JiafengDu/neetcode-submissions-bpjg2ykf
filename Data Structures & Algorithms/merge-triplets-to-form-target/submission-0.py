class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        has_x = has_y = has_z = False
        tx, ty, tz = target

        for a, b, c in triplets:
            if a > tx or b>ty or c>tz:
                continue
            
            if a == tx:
                has_x = True
            if b == ty:
                has_y = True
            if c == tz:
                has_z = True
            
            if has_x and has_y and has_z:
                return True
            
        return has_x and has_y and has_z