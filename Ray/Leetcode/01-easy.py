'''
You are given an integer array nums.

Return true if the frequency of any element of the array is prime, otherwise, return false.

The frequency of an element x is the number of times it occurs in the array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.
'''

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            if freq.get(i):
                freq[i] += 1
            else:
                freq[i] = 1
        # print(f'{freq} \n')

        for key, val in freq.items():
            if val > 1:
                for j in range(2, val):
                    if val % j == 0:
                        break
                else:
                    return True
        else:
            return False