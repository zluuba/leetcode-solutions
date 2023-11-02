# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average
# of the values in its subtree.
# Note:
#  - The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
#  - A subtree of root is a tree consisting of root and all of its descendants.

# Example 1:
# Input: root = [4,8,5,0,1,null,6]
# Output: 5
# Explanation:
# For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
# For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
# For the node with value 0: The average of its subtree is 0 / 1 = 0.
# For the node with value 1: The average of its subtree is 1 / 1 = 1.
# For the node with value 6: The average of its subtree is 6 / 1 = 6.

# Example 2:
# Input: root = [1]
# Output: 1
# Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

# --------------- Runtime 45 ms, beats 78.74%. Memory 17.6MB, beats 28.7% ---------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, res):
            if not node:
                return 0, 0, res

            left_count, left_sum, res = dfs(node.left, res)
            right_count, right_sum, res = dfs(node.right, res)

            count = left_count + right_count + 1
            summ = left_sum + right_sum + node.val

            if summ // count == node.val:
                res += 1

            return count, summ, res

        *_, result = dfs(root, 0)
        return result
