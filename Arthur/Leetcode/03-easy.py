# Problem: Check If N and Its Double Exist
# Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/
# Note: 

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for n in arr:
            if n*2 in seen or n/2 in seen:
                return True
            seen.add(n)
        return False
