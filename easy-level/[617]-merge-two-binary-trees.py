# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped
# while the others are not. You need to merge the two trees into a new binary tree.
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.

# Example 1:
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]

# Example 2:
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]

# --------------- Runtime 85 ms, beats 59.71%. Memory 15.4MB, beats 69.55% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        if not root1 or not root2:
            return root1 if root1 else root2

        tree = TreeNode(root1.val + root2.val)

        tree.left = self.mergeTrees(root1.left, root2.left)
        tree.right = self.mergeTrees(root1.right, root2.right)

        return tree


# Alternative solution. Just bigger, nothing more
# --------------- Runtime 92 ms, beats 27.5%. Memory 15.7MB, beats 15.60% ---------------


class Solution2:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return

        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0

        left1, right1 = (root1.left, root1.right) if root1 else (None, None)
        left2, right2 = (root2.left, root2.right) if root2 else (None, None)

        tree = TreeNode(val1 + val2)

        tree.left = self.mergeTrees(left1, left2)
        tree.right = self.mergeTrees(right1, right2)

        return tree
