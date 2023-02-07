# You are given the root of a binary tree that consists
# of exactly 3 nodes: the root, its left child, and its right child.
#
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

# --------------- Runtime 35 ms, beats 59.2%. Memory 13.8MB, beats 92.29% ---------------


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root:
            return root.val == sum([root.left.val, root.right.val])
        return False
