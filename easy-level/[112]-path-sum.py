# https://leetcode.com/problems/path-sum/

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.

# --------------- Runtime 61 ms, beats 84.66%. Memory 15.2MB, beats 41.36% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def search(node, curr):
            if not node:
                return False

            next_curr = curr + node.val

            if next_curr == targetSum and (not node.left and not node.right):
                return True
            return any([search(node.left, next_curr), search(node.right, next_curr)])

        return search(root, 0)
