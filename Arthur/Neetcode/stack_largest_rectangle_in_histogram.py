# Problem: Largest Rectangle in Histogram
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Note: i hated this question (optimal) passionately.

# Single pass solution
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        res = 0
        heights.append(0)
        
        for ir in range(len(heights)):
            while st and heights[ir] < heights[st[-1]]:
                h = heights[st.pop()]
                left = st[-1] if st else -1
                width = ir - left - 1
                res = max(res, h * width)
            st.append(ir)

        return res

# Three pass solution, slower but easier to read
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)

#         # left bounds
#         st = [] # reductive indices
#         lMax = [0] * n
#         for i in range(n):
#             while st and heights[i] <= heights[st[-1]]:
#                 st.pop()
#             if st:
#                 lMax[i] = st[-1] + 1
#             st.append(i)

#         # right bounds
#         st = []
#         rMax = [n-1] * n
#         for i in range(n-1, -1, -1):
#             while st and heights[i] <= heights[st[-1]]:
#                 st.pop()
#             if st:
#                 rMax[i] = st[-1] - 1
#             st.append(i)

#         res = 0
#         for i in range(n):
#             res = max(res, heights[i] * (rMax[i] - lMax[i] + 1))

#         return res
