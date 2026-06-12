class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position of ith car, - taget = remain
        remain = [(target - p, s) for p, s in zip(position, speed)]
        remain.sort()
        
        fleets = []
        for dist, s in remain:
            time = dist / s
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)


        # remain = [(6,2),(9,3)]
        # first car is start of fleet, can second catch up to first?
        # 6/2=3 is the time for first car to reach target
        # 9/3=3 is the time for second car to reach target
        # if curr_time_taken <= prev_time_taken, second one belong to the same fleet
        # prev_time_taken needs to be updated to NEW.