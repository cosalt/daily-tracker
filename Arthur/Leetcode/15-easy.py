# Problem: Longer Contiguous Segments of Ones than Zeros
# Link: https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
# Note:

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        con_zero, con_one, cur_count = 0, 0, 0

        prev = None
        for c in s:
            if c == prev:
                cur_count += 1
            else:
                cur_count = 1
                prev = c
                
            if prev == '1':
                con_one = max(con_one, cur_count)
            else:
                con_zero = max(con_zero, cur_count)

        return con_one > con_zero
    
