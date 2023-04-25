# https://leetcode.com/problems/triangle/

# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

# Example 2:
# Input: triangle = [[-10]]
# Output: -10

# --------------- Runtime 65 ms, beats 78.69%. Memory 14.8MB, beats 99.57% ---------------
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        dp = triangle[-1]

        for i in range(length - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]
