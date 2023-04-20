# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

# A cell (r, c) of an Excel sheet is represented as a string "<col><row>" where:
# - <col> denotes the column number c of the cell. It is represented by alphabetical letters.
#       - For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
# - <row> is the row number r of the cell. The rth row is represented by the integer r.

# You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1,
# <row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2,
# such that r1 <= r2 and c1 <= c2.

# Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2.
# The cells should be represented as strings in the format mentioned above and be sorted in
# non-decreasing order first by columns and then by rows.

# Example 1:
# Input: s = "K1:L2"
# Output: ["K1","K2","L1","L2"]
# Explanation:
# The above diagram shows the cells which should be present in the list.
# The red arrows denote the order in which the cells should be presented.

# Example 2:
# Input: s = "A1:F1"
# Output: ["A1","B1","C1","D1","E1","F1"]
# Explanation:
# The above diagram shows the cells which should be present in the list.
# The red arrow denotes the order in which the cells should be presented.

# --------------- Runtime 43 ms, beats 60.90%. Memory 13.9MB, beats 60.90% ---------------
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start_cell, end_cell = s.split(':')

        result = []
        for i in range(ord(start_cell[0]), ord(end_cell[0]) + 1):
            for j in range(int(start_cell[1]), int(end_cell[1]) + 1):
                cell = chr(i) + str(j)
                result.append(cell)

        return result


# Alternative solution. Without ord() function.
# Also used with string lib (ascii_uppercase)
# --------------- Runtime 44 ms, beats 54.63%. Memory 14MB, beats 16.74% ---------------


class Solution2:
    def cellsInRange(self, s: str) -> List[str]:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        start_cell, end_cell = s.split(':')
        chunk = letters.index(start_cell[0]), letters.index(end_cell[0])

        result = []
        for i in range(chunk[0], chunk[1] + 1):
            for j in range(int(start_cell[1]), int(end_cell[1]) + 1):
                cell = letters[i] + str(j)
                result.append(cell)

        return result
