# Problem: Count Number of Trapezoids I
# Link: https://leetcode.com/problems/count-number-of-trapezoids-i/
# Note: Initial solution correctly pre-computed combinations, but still resulted in TLE
#       due to O(Y^2).
#       Next solution had some key improvements:
#       - Used a suffix sum array and reductive ways variable as the problem could be 
#         reduced to:
#            w1 * (sum w2 -> wn) + w2 * (sum w3 -> wn) + ... + wn-1 * wn
#       - Only the per-level frequency is needed, so instead creating a map of x grouped 
#         by y, used Counter to get immediate frequency map.
#       - Calculating line combinations could be reduced with list comprehension.

from collections import Counter

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Y-level frequency map
        y_freq = Counter(point[1] for point in points)

        # Number of line combinations
        ways = [freq*(freq-1)//2 for freq in y_freq.values()]

        # Calculate total pairs for each possible line
        ways_total = sum(ways)
        total = 0
        for way in ways:
            ways_total -= way
            total += way * ways_total

        return total % MOD

# First solution (TLE)

# from collections import defaultdict

# class Solution:
#     def countTrapezoids(self, points: List[List[int]]) -> int:
#         MOD = 10**9 + 7

#         # Group by y
#         y_to_x = defaultdict(list)
#         for x, y in points:
#             y_to_x[y].append(x)

#         # Number of possible lines
#         ways = []
#         for xs in y_to_x.values():
#             n = len(xs)
#             ways.append(n * (n - 1) // 2)

#         # Calculate total pairs for each possible line
#         ways_total = sum(ways)
#         total = 0
#         for way in ways:
#             ways_total -= way
#             total += way * ways_total

#         # Old pair calculation (no suffix sum array)
#         # sorted_keys = sorted(y_to_x)
#         # for i in range(len(sorted_keys) - 1):
#         #     y_a = sorted_keys[i]
#         #     y_a_ways = y_to_x[y_a]
#         #     for j in range(i + 1, len(sorted_keys)):
#         #         y_b = sorted_keys[j]
#         #         count += y_a_ways * y_to_x[y_b]

#         return total % MOD
