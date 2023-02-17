# Given the root of a Binary Search Tree (BST),
# return the minimum difference between the values of any two different nodes in the tree.

# --------------- Runtime 39 ms, beats 35.31%. Memory 13.8MB, beats 74.83% ---------------


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

        sort_nums = sorted(nums)
        result = max(sort_nums)
        for ind, num in enumerate(sort_nums[:-1]):
            result = min(sort_nums[ind + 1] - num, result)

        return result
