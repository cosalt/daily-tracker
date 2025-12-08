# Problem: Count Odd Numbers in an Interval Range
# Link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range
# Notes: Both solsrun at effectively same speed (got better results on mine? but shouldn't)

class Solution:
    # My sol
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (high % 2 == 1 or low % 2 == 1)

    # Model sol
    # def countOdds(self, low: int, high: int) -> int:
    #     return (high + 1) // 2 - low // 2
