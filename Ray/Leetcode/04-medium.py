'''

You are given a 0-indexed integer array coins, representing the values of the coins available, and an integer target.

An integer x is obtainable if there exists a subsequence of coins that sums to x.

Return the minimum number of coins of any value that need to be added to the array so that every integer in the range [1, target] is obtainable.

A subsequence of an array is a new non-empty array that is formed from the original array by deleting some (possibly none) of the elements without disturbing the relative positions of the remaining elements.

'''
from typing import List
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        range = 0
        coins = []

        for i in range(coins):
            if coins[i] <= range + 1:
                range += coins[i]
            else:
                while coins[i] > range + 1:
                    coins.append(range + 1)
                    range += range + 1
                range += coins[i]
        return len(coins)
    
