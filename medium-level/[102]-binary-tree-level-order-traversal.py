# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# --------------- Runtime 36 ms, beats 68.67%. Memory 14.2MB, beats 42.97% ---------------
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack, result = [root], []

        while stack:
            length, level = len(stack), []

            for i in range(length):
                node = stack.pop(0)
                if node:
                    level.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)

            if level:
                result.append(level)

        return result
