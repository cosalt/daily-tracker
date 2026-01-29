class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        area = []

        while left < right:
            currArea = (right - left) * min(heights[right], heights[left])
            area.append(currArea)

            if heights[left] < heights[right]:    left += 1
            else:                               right -= 1
        print(area)
        return max(area)
