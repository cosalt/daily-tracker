"""
Problem: https://neetcode.io/problems/two-integer-sum?list=neetcode150

Description:
    Given an array of integers nums and 
    an integer target, return the indices 
    i and j such that 
    nums[i] + nums[j] == target and i != j.

    You may assume that every input has exactly 
    one pair of indices i and j that satisfy 
    the condition.

    Return the answer with the smaller index first. 

Examples:
    Example 1:
        Input: nums = [3,4,5,6], target = 7

        Output: [0,1]

    Example 2:
        Input: nums = [4,5,6], target = 10

        Output: [0,2]


Recommended Time & Space Complexity:
    Time:   O(n)
    Space:  O(n)
"""
from typing import List
class Solution1:
    """
    Hash Map Two pass

    Time & Space Complexity Achieved:
        Time: O(n)
    
        Space: O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in indices:
                return [indices[difference], i]

            indices[num] = i
