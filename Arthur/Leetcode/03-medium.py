# Problem: Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/
# Note: Can be improved with Manacher's algorithm, but expand-around-center
#       seemed ample.
#       Most optimisation came from tracking index values for comparison and
#       only creating a substring (expensive) at the end.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = None
        for i in range(len(s)):
            for j in (0,1):
                l = i
                r = i+j
                cur = ""

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                l += 1
                r -= 1

                if not res or r - l + 1 > res[1] - res[0] + 1:
                    res = l, r

        return s[res[0]:res[1]+1]
