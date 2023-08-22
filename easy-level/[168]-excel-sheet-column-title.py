# https://leetcode.com/problems/excel-sheet-column-title/

# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
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
# Input: columnNumber = 1
# Output: "A"

# Example 2:
# Input: columnNumber = 28
# Output: "AB"

# Example 3:
# Input: columnNumber = 701
# Output: "ZY"

# --------------- Runtime 41 ms, beats 59.31%. Memory 16.3MB, beats 63.20% ---------------
import string


class Solution:
    def convertToTitle(self, num: int) -> str:
        abc = string.ascii_uppercase
        abc_len = len(abc)
        res = ''

        while num > 0:
            remainder = num % abc_len
            res = abc[remainder - 1] + res
            num = (num - 1) // abc_len

        return res
