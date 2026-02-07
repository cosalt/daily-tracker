# Problem: Valid Perfect Square
# Link: https://leetcode.com/problems/valid-perfect-square/
# Note: 

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num**0.5 % 1 == 0
