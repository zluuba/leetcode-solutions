# https://leetcode.com/problems/pascals-triangle-ii/

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

# --------------- Runtime 31 ms, beats 71.67%. Memory 13.8MB, beats 93.55% ---------------
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []

        for i in range(rowIndex + 1):
            row_length = i + 1
            curr_row = [1] * row_length

            if row_length > 2:
                for j in range(1, row_length - 1):
                    curr_row[j] = row[j - 1] + row[j]

            row = curr_row

        return row


# Alternative solution with the construction of a full triangle
# --------------- Runtime 61 ms, beats 84.66%. Memory 15.2MB, beats 41.36% ---------------

class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []

        for i in range(rowIndex + 1):
            row_length = i + 1
            row = [1] * row_length

            if row_length > 2:
                for j in range(1, row_length - 1):
                    row[j] = triangle[i-1][j - 1] + triangle[i-1][j]

            triangle.append(row)

        return triangle[-1]
