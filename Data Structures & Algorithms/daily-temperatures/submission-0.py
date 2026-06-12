import collections
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if we see a hotter temp, 
        # we can remove all element , 
        # iterate through temp, keep a list/structure, 
        # if curr temp bigger than elements in list, remove/add to result
        # else, curr temp is smaller than before, add to list/structure
        deque = collections.deque()
        res = [0]*len(temperatures)
        # 30,38,30,36,35,40,28
        # first put 30 to deque, then we see 38
        for i, temp in enumerate(temperatures):
            while deque and temperatures[deque[-1]] < temp:
                smaller_temp_idx = deque.pop()
                res[smaller_temp_idx] = i-smaller_temp_idx
            
            deque.append(i)
        
        return res