# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
# (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Example:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#                [0,0,0,0,0,0,0,1,1,1,0,0,0],
#                [0,1,1,0,1,0,0,0,0,0,0,0,0],
#                [0,1,0,0,1,1,0,0,1,0,1,0,0],
#                [0,1,0,0,1,1,0,0,1,1,1,0,0],
#                [0,0,0,0,0,0,0,0,0,0,1,0,0],
#                [0,0,0,0,0,0,0,1,1,1,0,0,0],
#                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# --------------- Runtime 113 ms, beats 99.8%. Memory 16.4MB, beats 71.62% ---------------
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def search(row, col, area=0):
            if row < 0 or col < 0 or row == rows or col == cols:
                return area
            if grid[row][col] == 0:
                return area

            area += 1
            grid[row][col] = 0    # mark as visited

            area += search(row + 1, col)
            area += search(row - 1, col)
            area += search(row, col + 1)
            area += search(row, col - 1)
            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = search(row, col)
                    max_area = max(max_area, area)

        return max_area
