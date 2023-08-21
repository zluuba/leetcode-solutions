# https://leetcode.com/problems/same-tree/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# --------------- Runtime 40 ms, beats 71.88%. Memory 16.3MB, beats 55.17% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = [p] if p else []
        stack2 = [q] if q else []

        if len(stack1) != len(stack2):
            return False

        while stack1 and stack2:
            node1 = stack1.pop(0)
            node2 = stack2.pop(0)

            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False

            stack1.extend([node1.left, node1.right])
            stack2.extend([node2.left, node2.right])

        return True
