# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value.

# --------------- Runtime 52 ms, beats 71.54%. Memory 16.3MB, beats 38.32% ---------------
from typing import List


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def get_value(node):
            if not node:
                return

            result.append(node.val)
            for child in node.children:
                get_value(child)

        get_value(root)
        return result
