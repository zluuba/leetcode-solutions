# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s)
# (i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:
#  - The left subtree of a node contains only nodes with keys less than or equal to the node's key.
#  - The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
#  - Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]

# Example 2:
# Input: root = [0]
# Output: [0]

# --------------- Runtime 58 ms, beats 47.1%. Memory 20.7MB, beats 36.15% ---------------
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        values_count = dict()
        nodes = [root]

        while nodes:
            node = nodes.pop(0)

            if not node:
                continue

            values_count[node.val] = values_count.get(node.val, 0) + 1
            nodes.extend([node.left, node.right])

        max_count = max(values_count.values())
        result = [value for value, count in values_count.items() if count == max_count]
        return result
