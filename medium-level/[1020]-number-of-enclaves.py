# https://leetcode.com/problems/number-of-enclaves/

# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell
# or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

# Example 1:
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

# Example 2:
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.

# --------------- Runtime 629 ms, beats 88.42%. Memory 75.9MB, beats 53.48% ---------------
from typing import List


# Solution with grid modify
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # sink the island if we can walk off the boundary of the grid on it
        def sink_the_island(row, col):
            if row > rows - 1 or col > cols - 1 or row < 0 or col < 0:
                return
            if grid[row][col] == 0:
                return

            grid[row][col] = 0
            sink_the_island(row + 1, col)
            sink_the_island(row - 1, col)
            sink_the_island(row, col + 1)
            sink_the_island(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    if grid[row][col] == 1:
                        sink_the_island(row, col)

        enclaves = sum(map(sum, grid))
        return enclaves


# --------------- Runtime 737 ms, beats 47.11%. Memory 86MB, beats 23.95% ---------------

# Alternative solution without grid modify
class Solution2:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0:
                return 0
            if grid[row][col] == 0 or (row, col) in visit:
                return 0

            visit.add((row, col))
            result = 1 + sum([
                dfs(row + 1, col), dfs(row - 1, col),
                dfs(row, col + 1), dfs(row, col - 1)
            ])
            return result

        enclaves = 0
        for row in range(rows):
            for col in range(cols):
                enclaves += grid[row][col]

                if grid[row][col] == 1 and (row, col) not in visit:
                    if row in [0, rows - 1] or col in [0, cols - 1]:
                        enclaves -= dfs(row, col)

        return enclaves
