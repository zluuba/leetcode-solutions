# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# --------------- Runtime 68 ms, beats 12.56%. Memory 16.4MB, beats 72.79% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return check(node.left, left, node.val) and check(node.right, node.val, right)

        return check(root, -2 ** 32, 2 ** 32)
