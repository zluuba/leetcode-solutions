# Given an integer numRows, return the first numRows of Pascal's triangle.

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

# --------------- Runtime 30 ms, beats 88.73%. Memory 13.8MB, beats 96.33% ---------------
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            row_length = len(row)
            if row_length > 2:
                for j in range(row_length):
                    if j != 0 and j != row_length - 1:
                        row[j] = triangle[i-1][j - 1] + triangle[i-1][j]
            triangle.append(row)

        return triangle
