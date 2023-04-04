# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Example 1:
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# Example 2:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19

# --------------- Runtime 201 ms, beats 77.52%. Memory 17.7MB, beats 60% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depths = {}

        def dfs(node, depth):
            depths[depth] = depths.get(depth, 0) + node.val

            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 0)
        max_depth = max(depths.keys())
        return depths[max_depth]
