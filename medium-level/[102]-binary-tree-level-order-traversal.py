# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

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
