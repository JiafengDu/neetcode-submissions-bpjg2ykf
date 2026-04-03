class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step_one = 0 # min future cost if take one step up
        step_two = 0 # min future cost if take two steps up 

        for i in range(len(cost)-1, -1, -1):
            current_cost = cost[i] + min(step_one, step_two)
            step_two = step_one
            step_one = current_cost
        
        return min(step_one, step_two)