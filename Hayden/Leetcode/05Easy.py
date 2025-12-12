# Problem: https://leetcode.com/problems/sort-integers-by-binary-reflection/
class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        # Refelects integer from its binary 
        def reflect(num: int) -> int:
            # ignore 0b prefix
            return int(bin(num)[2:][::-1], 2)
        # Return by custom key
        return sorted(nums, key=lambda num: (reflect(num), num))
