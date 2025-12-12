# Problem: Sort Integers by Binary Reflection
# Link: https://leetcode.com/problems/sort-integers-by-binary-reflection/
# Note: 

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        reflect = lambda num: int(bin(num)[-1:1:-1], 2)
        nums.sort(key=lambda num: (reflect(num), num))
        return nums
