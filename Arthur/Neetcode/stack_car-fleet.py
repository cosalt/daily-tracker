# Problem: Car Fleet
# Link: https://leetcode.com/problems/car-fleet/
# Note: use zip() to pair iterators

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        cars.sort(reverse=True)

        times_st = []
        for position, speed in cars:
            time_to_target = (target - position) / speed

            if not times_st or times_st[-1] < time_to_target:
                times_st.append(time_to_target)
        
        return len(times_st)
