# Problem: Count Distinct Numbers on Board
# Link: https://leetcode.com/problems/count-distinct-numbers-on-board/
# Note: whatever tf this problem was

class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n == 1:
            return 1
        return n-1
