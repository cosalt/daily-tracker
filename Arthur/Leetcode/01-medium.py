# Problem: Count Number of Rectangles Containing Each Point
# Links: https://leetcode.com/problems/count-number-of-rectangles-containing-each-point
# Note: ~

from collections import defaultdict
from bisect import bisect_left

MAX_HEIGHT = 100

# Brute force

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        count = [0] * len(points)
        for i, point in enumerate(points):
            for rectangle in rectangles:
                count[i] += (0 <= point[0] <= rectangle[0] and 0 <= point[1] <= rectangle[1])

        return count

# Best attempt
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        widths = defaultdict(list)
        for width, height in rectangles:
            widths[height].append(width)
        
        for height in widths.keys():
            widths[height].sort()

        result = [0] * len(points)
        for i, (x, y) in enumerate(points):
            for height in widths.keys():
                if height < y:
                    continue
                least_ge = self.leftmost_ge(widths[height], x)
                if least_ge >= 0:
                    result[i] += len(widths[height]) - least_ge

        return result

    def leftmost_ge(self, arr: List[int], t: int):
        l, r = 0, len(arr) - 1
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if arr[m] >= t:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans

# Improved with bisect_left (compiled C library, same logic)
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        widths = defaultdict(list)
        for w, h in rectangles:
            widths[h].append(w)
        
        for h in widths:
            widths[h].sort()

        res = [0] * len(points)
        for i, (x, y) in enumerate(points):
            for h in range(y, MAX_HEIGHT + 1):
                arr = widths[h]
                if not arr: continue
                least_ge = bisect_left(arr, x)
                res[i] += len(arr) - least_ge

        return res
