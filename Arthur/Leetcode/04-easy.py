# Problem: Largest Odd Number in String
# Link: https://leetcode.com/problems/largest-odd-number-in-string/
# Note: Faster to use string membership than python mod op

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for r in range(len(num)-1, -1, -1):
            if num[r] in "13579":
                return num[:r+1]
        return ""
