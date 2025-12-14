# Problem: Merge Two 2D Arrays by Summing Values
# Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
# Note: 

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1 = p2 = 0
        n1, n2 = len(nums1), len(nums2)
        res = []
        while p1 < n1 and p2 < n2:
            id1, val1 = nums1[p1]
            id2, val2 = nums2[p2]

            if id1 == id2:
                res.append([id1, val1 + val2])
                p1 += 1
                p2 += 1
            elif id1 < id2:
                res.append([id1, val1])
                p1 += 1
            else:
                res.append([id2, val2])
                p2 += 1
        
        res.extend(nums1[p1:])
        res.extend(nums2[p2:])

        return res
