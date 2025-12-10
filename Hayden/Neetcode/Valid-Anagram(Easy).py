"""
Problem: https://neetcode.io/problems/is-anagram?list=neetcode150

Description:
    Given two strings s and t, return true if the two 
    strings are anagrams of each other, otherwise 
    return false.

    An anagram is a string that contains the exact 
    same characters as another string, but the order of 
    the characters can be different.

Examples:
    Example 1:
        Input: s = "racecar", t = "carrace"

        Output: true
    Example 2:
        Input: s = "jar", t = "jam"

        Output: false

Recommended Time & Space Complexity:
    Time: O(n + m)
    Space: O(1)
    n = Length of the string `s`
    m = Lenght of the string `t`
"""

class Solution1:
    """
    Brute forced

    Time & Space Complexity Achieved:
        Time: O(nlogn + mlogm)
        Space: O(1)
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """Returns true if both sorted anagrams are equal"""
        return (sorted(s) == sorted(t))

class Solution2:
    """
    Hash Map

    Time & Space Complexity Achieved:
        Time: O(n + m)
        Space: O(1)
    """

    def isAnagram(self, s: str, t: str) -> bool:
        # Hash table declaration
        sFreq, tFreq = {}, {}

        # Base Case
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sFreq[s[i]] = sFreq.get(s[i], 0) + 1
            tFreq[t[i]] = tFreq.get(t[i], 0) + 1
        
        return sFreq == tFreq
