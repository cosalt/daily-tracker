# Problem: Check if Any Element Has Prime Frequency
# Link: https://leetcode.com/problems/check-if-any-element-has-prime-frequency
# Note: ~

from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for freq in counts.values():
            if self.isPrime(freq): return True
        return False

    def isPrime(self, num: int) -> bool:
        if num == 1: return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0: return False
        return True
