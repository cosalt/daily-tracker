"""
You are given a 2D integer array rectangles where rectangles[i] = [li, hi] indicates that ith rectangle has a length of li and a height of hi. You are also given a 2D integer array points where points[j] = [xj, yj] is a point with coordinates (xj, yj).

The ith rectangle has its bottom-left corner point at the coordinates (0, 0) and its top-right corner point at (li, hi).

Return an integer array count of length points.length where count[j] is the number of rectangles that contain the jth point.

The ith rectangle contains the jth point if 0 <= xj <= li and 0 <= yj <= hi. Note that points that lie on the edges of a rectangle are also considered to be contained by that rectangle.
"""

from typing import List


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        contains_rectangles = []
        for i in range(len(points)):
            count = 0
            x = points[i][0]
            y = points[i][1]
            for j in range(len(rectangles)):
                if x <= rectangles[j][0] and y <= rectangles[j][1]:
                    count += 1
            contains_rectangles.append(count)
        return contains_rectangles


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Basic case
    rectangles1 = [[1,2],[2,3],[2,5]]
    points1 = [[2,1],[1,4]]
    print(f"Test 1:")
    print(f"Rectangles: {rectangles1}")
    print(f"Points: {points1}")
    print(f"Result: {solution.countRectangles(rectangles1, points1)}")
    print(f"Expected: [2, 1]")
    print()
    
    # Test 2: All points contained
    rectangles2 = [[5,5],[10,10]]
    points2 = [[1,1],[3,3]]
    print(f"Test 2:")
    print(f"Rectangles: {rectangles2}")
    print(f"Points: {points2}")
    print(f"Result: {solution.countRectangles(rectangles2, points2)}")
    print(f"Expected: [2, 2]")
    print()
    
    # Test 3: No points contained
    rectangles3 = [[1,1],[2,2]]
    points3 = [[5,5],[10,10]]
    print(f"Test 3:")
    print(f"Rectangles: {rectangles3}")
    print(f"Points: {points3}")
    print(f"Result: {solution.countRectangles(rectangles3, points3)}")
    print(f"Expected: [0, 0]")
    print()
    
    # Test 4: Points on edges (should be contained)
    rectangles4 = [[3,3]]
    points4 = [[0,0],[3,3],[3,0],[0,3]]
    print(f"Test 4:")
    print(f"Rectangles: {rectangles4}")
    print(f"Points: {points4}")
    print(f"Result: {solution.countRectangles(rectangles4, points4)}")
    print(f"Expected: [1, 1, 1, 1]")