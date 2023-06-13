# https://leetcode.com/problems/equal-row-and-column-pairs/

# Given a 0-indexed n x n integer matrix grid,
# return the number of pairs (ri, cj) such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

# Example 1:
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]

# Example 2:
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

# --------------- Runtime 701 ms, beats 26.93%. Memory 21.7MB, beats 41.9% ---------------
from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = 0
        length = len(grid)
        flipped_grid = [list(i) for i in zip(*grid)]

        for i in range(length):
            for j in range(length):
                if grid[i] == flipped_grid[j]:
                    counter += 1

        return counter


# Alternative solution - fastest
# --------------- Runtime 460 ms, beats 98.30%. Memory 21.8MB, beats 26.88% ---------------

class Solution2:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = 0
        c = Counter(tuple(row) for row in grid)

        for col in zip(*grid):
            counter += c[col]

        return counter


# Alternative solution - exotic
# --------------- Runtime 819 ms, beats 14.57%. Memory 21.9MB, beats 26.88% ---------------

class Solution3:
    def equalPairs(self, grid: List[List[int]]) -> int:
        flipped_grid = [i for i in zip(*grid)]
        result = [
            1 for j in range(len(grid))
            for i in range(len(grid))
            if tuple(grid[i]) == flipped_grid[j]
        ]

        return sum(result)
