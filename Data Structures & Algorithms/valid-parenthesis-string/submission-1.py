class Solution:
    def checkValidString(self, s: str) -> bool:
        # treat all * as '(' 
        # or treat all * as ')'
        # ((***)
        left_min, left_max = 0, 0

        for c in s:
            if c == "(":
                left_min += 1
                left_max += 1
            elif c == ")":
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
        
            if left_max < 0: # too many ")"
                return False
            
            if left_min < 0:
                left_min = 0
        
        return left_min == 0