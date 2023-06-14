# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values
# of any two different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# --------------- Runtime 67 ms, beats 67.32%. Memory 18.7MB, beats 15.28% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values, stack = [], [root]

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)
                values.append(node.val)

        values.sort()
        result = float('inf')

        for i in range(len(values) - 1):
            diff = values[i + 1] - values[i]
            result = min(result, diff)

            if result == 1:
                break

        return result
