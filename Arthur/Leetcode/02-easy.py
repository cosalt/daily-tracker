# Problem: Maximum Sum With Exactly K Elements
# Link: https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
# Note: 

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        x = max(nums)
        return ((k-1)*k)//2+x*k
