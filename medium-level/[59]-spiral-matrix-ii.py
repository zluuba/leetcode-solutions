# https://leetcode.com/problems/spiral-matrix-ii/

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# --------------- Runtime 53 ms, beats 5.44%. Memory 16.4MB, beats 5.62% ---------------
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1

        while num <= n * n:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

        return matrix
