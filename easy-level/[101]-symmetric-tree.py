# https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# --------------- Runtime 41 ms, beats 29.46%. Memory 13.8MB, beats 90.34% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compare(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False

        return all([self.compare(node1.left, node2.right),
                    self.compare(node2.left, node1.right)])

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root, root)
