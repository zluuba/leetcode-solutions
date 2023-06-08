# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
# return the number of negative numbers in grid.

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0

# --------------- Runtime 139 ms, beats 21.47%. Memory 17.5MB, beats 44.5% ---------------
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = [row for row in grid for num in row if num < 0]
        return len(negatives)
