# Problem: 2656. Maximum Sum With Exactly K Elements
# Challenge: https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return (k*max(nums) + (k*(k-1)//2))

