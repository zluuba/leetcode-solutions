# Given the root of a Binary Search Tree (BST),
# return the minimum difference between the values of any two different nodes in the tree.

# --------------- Runtime 30 ms, beats 85.90%. Memory 14MB, beats 32.63% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                nums.append(node.val)

        nums.sort()
        result = max(nums)
        for ind, num in enumerate(nums[:-1]):
            result = min(nums[ind + 1] - num, result)

        return result
