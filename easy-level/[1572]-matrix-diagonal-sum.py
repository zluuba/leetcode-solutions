# https://leetcode.com/problems/matrix-diagonal-sum/

# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal
# that are not part of the primary diagonal.

# Example 1:
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

# Example 2:
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8

# Example 3:
# Input: mat = [[5]]
# Output: 5

# --------------- Runtime 117 ms, beats 23.28%. Memory 16.6MB, beats 11.57% ---------------
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        p1, p2 = 0, len(mat[0]) - 1

        for row in mat:
            if p1 == p2:
                result += row[p1]
            else:
                result += row[p1] + row[p2]

            p1 += 1
            p2 -= 1

        return result
