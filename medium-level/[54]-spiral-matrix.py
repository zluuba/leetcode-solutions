# https://leetcode.com/problems/spiral-matrix/

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# --------------- Runtime 35 ms, beats 50.38%. Memory 16.3MB, beats 14.84% ---------------
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result.extend(matrix[0])
            matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]

        return result


# Alternative solution - without zip function
# --------------- Runtime 42 ms, beats 14.92%. Memory 16.2MB, beats 14.84% ---------------

class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def flip(mat):
            new_mat = []

            for i in range(len(mat[0]) - 1, -1, -1):
                new_row = []
                for j in range(len(mat)):
                    new_row.append(mat[j][i])
                new_mat.append(new_row)

            return new_mat

        result = []
        while matrix:
            result.extend(matrix[0])
            matrix.pop(0)
            if matrix:
                matrix = flip(matrix)

        return result
