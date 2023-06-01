# https://leetcode.com/problems/shortest-path-in-binary-matrix/

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
# If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell
# (i.e., (n - 1, n - 1)) such that:
# - All the visited cells of the path are 0.
# - All the adjacent cells of the path are 8-directionally connected
#   (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1

# --------------- Runtime 627 ms, beats 61.37%. Memory 16.9MB, beats 38.28% ---------------
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        if len(grid) == len(grid[0]) == 1:
            return 1

        directions = ((1, 1), (0, 1), (1, 0), (-1, 1),
                      (-1, 0), (-1, -1), (0, -1), (1, -1))
        q = [(0, 0, 1)]
        grid[0][0] = 1

        while q:
            r, c, path = q.pop(0)
            if (r == (len(grid) - 1)) and (c == (len(grid[0]) - 1)):
                return path

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                    continue
                elif grid[row][col]:
                    continue

                grid[row][col] = 1
                q.append((row, col, path + 1))

        return -1
