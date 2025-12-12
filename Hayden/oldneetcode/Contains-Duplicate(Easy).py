"""
Problem: https://neetcode.io/problems/duplicate-integer?list=neetcode150

Description:
    Given an integer array nums, return true if any 
    value appears more than once in the array, 
    otherwise return false.

Examples:
    Example 1:
        Input: nums = [1, 2, 3, 3]

        Output: true
    Example 2:
        Input: nums = [1, 2, 3, 4]

        Output: false

Recommended Time & Space Complexity:
    Time: O(n)
    Space: O(n)
    n = size of input array
"""

from typing import List

class Solution:
    """
    Time & Space Complexity Achieved:
        Time: O(n)
        Space: O(n)
    """

    def hasDuplicate(self, nums: List[int]) -> bool:
        """Creates a set from nums (removes duplicates) and then compares length to original list"""
        return (len(set(nums)) != len(nums))

