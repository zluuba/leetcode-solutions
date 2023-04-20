# https://leetcode.com/problems/number-of-closed-islands/

# Given a 2D grid consists of 0s (land) and 1s (water).
# An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally
# (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.

# Example:
# Input: grid = [[1,1,1,1,1,1,1,0],
#                [1,0,0,0,0,1,1,0],
#                [1,0,1,0,1,1,1,0],
#                [1,0,0,0,0,1,0,1],
#                [1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: islands in gray are closed because they are completely surrounded by water (group of 1s).

# Example 2:
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1

# --------------- Runtime 121 ms, beats 89.67%. Memory 14.6MB, beats 39.95% ---------------
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def search(row, col):
            if row < 0 or col < 0 or row == rows or col == cols:
                return False
            if grid[row][col] == 1:
                return True

            grid[row][col] = 1           # mark as visited
            return (all([
                search(row + 1, col), search(row - 1, col),
                search(row, col + 1), search(row, col - 1),
            ]))

        closed_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and search(row, col):
                    closed_islands += 1

        return closed_islands
