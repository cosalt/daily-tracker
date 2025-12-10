"""
Problem: https://neetcode.io/problems/anagram-groups?list=neetcode150

Description:
    Given an array of strings strs, 
    group all anagrams together into 
    sublists. You may return the output 
    in any order.

    An anagram is a string that contains 
    the exact same characters as another 
    string, but the order of the characters 
    can be different.

Examples:
    Example 1:
        Input: strs = ["act","pots","tops","cat","stop","hat"]

        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    Example 2:
        Input: strs = ["x"]

        Output: [["x"]]

    Example 3:
        Input: strs = [""]

        Output: [[""]]
        


Recommended Time & Space Complexity:
    Time:   O(m * n)
    Space:  O(m)
"""

from typing import List

class Solution1:
    """
    Time & Space Complexity Achieved:
        Time: O(m * n)
    
        Space: O(m * n)
        Not the target space complexity
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for str in strs:
            freq = [0]*26

            for char in str:
                i = ord(char)-ord('a')
                freq[i] += 1

            key = tuple(freq)
            if key not in groups:
                groups[key] = []
            groups[key].append(str)
        
        return list(groups.values())
