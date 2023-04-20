# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down
# to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# --------------- Runtime 45 ms, beats 59.4%. Memory 16.2MB, beats 49.77% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Alternative solution. Without recursion
# --------------- Runtime 48 ms, beats 41.16%. Memory 15.3MB, beats 81.3% ---------------


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result
