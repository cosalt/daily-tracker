# Problem: Number of Bit Changes to Make Two Integers Equal
# Link: https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/
# Note: bit mask simplified readability, bitwise OR mask checks for invalid inputs (k contains
#       1 where n does not).
#       bit_count() returns the number of 1s in a numbers binary representation.

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n | k != n:
            return -1
        return (n & ~k).bit_count()


# class Solution:
#     def minChanges(self, n: int, k: int) -> int:
#         if n == k:
#             return 0
        
#         if n | k != n:
#             return -1
            
#         n, k = bin(n)[2:], bin(k)[2:]
#         max_len = max(len(n), len(k))
#         n = n.zfill(max_len)
#         k = k.zfill(max_len)
        
#         res = 0
#         for i in range(max_len):
#             if n[i] == '1' and k[i] == '0':
#                 res += 1

#         return res
