# Problem: Leaf-Similar Trees
# Link: https://leetcode.com/problems/leaf-similar-trees/
# Note: can be improved using the function generator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []
        
        def inorder(root: TreeNode, leaves: List[int]):
            if not root:
                return
            
            if not root.left and not root.right:
                leaves.append(root.val)
            
            inorder(root.left, leaves)
            inorder(root.right, leaves)

        inorder(root1, leaves1)
        inorder(root2, leaves2)

        return leaves1 == leaves2
