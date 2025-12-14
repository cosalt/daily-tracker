# Problem: Count Collisions on a Road
# Link: https://leetcode.com/problems/count-collisions-on-a-road/
# Note: didn't spot final optimisation... settled with the two-pointer before
#       checking optimal

class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L").rstrip("R")
        return len(directions) - directions.count("S")

# class Solution:
#     def countCollisions(self, directions: str) -> int:
#         l, r = 0, len(directions) - 1
#         while l <= r and directions[l] == "L": l += 1
#         while l <= r and directions[r] == "R": r -= 1
#         return sum(directions[i] != "S" for i in range(l, r+1))
                
