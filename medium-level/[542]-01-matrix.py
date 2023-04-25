# https://leetcode.com/problems/01-matrix/

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

# --------------- Runtime 606 ms, beats 78.25%. Memory 17.1MB, beats 64.52% ---------------
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        length_row, length_col = len(mat), len(mat[0])
        queue = []

        for i in range(length_row):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = 'o'

        for r, c in queue:
            for r1, c1 in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                newr = r + r1
                newc = c + c1

                if 0 <= newr < length_row and 0 <= newc < length_col:
                    if mat[newr][newc] == 'o':
                        mat[newr][newc] = mat[r][c] + 1
                        queue.append((newr, newc))
        return mat
