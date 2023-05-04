# https://leetcode.com/problems/excel-sheet-column-number/

# Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.
# For example:
#   A -> 1
#   B -> 2
#   C -> 3
#   ...
#   Z -> 26
#   AA -> 27
#   AB -> 28
#   ...

# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701

# --------------- Runtime 46 ms, beats 8.4%. Memory 16.3MB, beats 5.82% ---------------


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result, pointer = 0, 0

        for i in range(len(columnTitle) - 1, -1, -1):
            char = columnTitle[pointer]
            result += (26 ** i) * (ord(char) - 64)
            pointer += 1

        return result
