# Problem: Word Pattern
# Link: https://leetcode.com/problems/word-pattern/description/
# Note: 

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s) or len(set(pattern)) != len(set(s)):
            return False
            
        chr_map = {}
        for c, word in zip(pattern, s):
            if c not in chr_map:
                chr_map[c] = word
            elif chr_map[c] != word:
                return False
        
        return True
