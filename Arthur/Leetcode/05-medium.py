# Problem: Short Encoding of Words
# Link: https://leetcode.com/problems/short-encoding-of-words/
# Note: set.discard() removes need for existence check. 
#       Tree appraoch might net better runtime?

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        for word in words:
            chrs = len(word)
            for i in range(1, chrs):
                words_set.discard(word[i:chrs])
        
        res = 0
        for word in words_set:
            res += len(word) + 1
        
        return res
