# Problem: First Unique Character in a String
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/
# Note: 

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        return -1
