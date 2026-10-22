class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        current_fleet_time = 0

        for pos, speed in cars:
            arrival_time = (target-pos)/speed
            if arrival_time > current_fleet_time:
                fleets += 1
                current_fleet_time = arrival_time
        return fleets