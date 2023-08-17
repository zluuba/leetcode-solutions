# https://leetcode.com/problems/01-matrix/

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

# --------------- Runtime 498 ms, beats 93.75%. Memory 19MB, beats 84.36% ---------------
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        queue = []

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = 'o'

        for r, c in queue:
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if 0 <= row < rows and 0 <= col < cols:
                    if mat[row][col] == 'o':
                        mat[row][col] = mat[r][c] + 1
                        queue.append((row, col))
        return mat
