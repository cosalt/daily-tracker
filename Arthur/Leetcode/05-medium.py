# Problem: Short Encoding of Words
# Link: https://leetcode.com/problems/short-encoding-of-words/
# Note: set.discard() removes need for existence check. 
#       Tree appraoch might net better runtime?

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        for word in words:
            if not word in words_set:
                continue

            for i in range(1, len(word)):
                words_set.discard(word[i:])
        
        return sum(len(word) + 1 for word in words_set)
