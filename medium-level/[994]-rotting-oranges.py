# https://leetcode.com/problems/rotting-oranges/

# You are given an m x n grid where each cell can have one of three values:
# - 0 representing an empty cell,
# - 1 representing a fresh orange, or
# - 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten,
# because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# --------------- Runtime 53 ms, beats 61.24%. Memory 13.9MB, beats 35.82% ---------------
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit, curr = [], []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.append((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))

        result = 0
        while visit and curr:
            for _ in range(len(curr)):
                i, j = curr.pop(0)

                for coord in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if coord in visit:
                        visit.remove(coord)
                        curr.append(coord)
            result += 1

        return -1 if visit else result
