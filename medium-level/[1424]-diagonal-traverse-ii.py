# https://leetcode.com/problems/diagonal-traverse-ii/

# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

# Example 1:
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]

# Example 2:
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

# --------------- Runtime 768 ms, beats 86.90%. Memory 41.3MB, beats 35.88% ---------------
from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        sum_of_indxs = defaultdict(list)
        result = []

        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                sum_of_indxs[i + j].append(num)

        for items in sum_of_indxs.values():
            result.extend(items[::-1])

        return result
