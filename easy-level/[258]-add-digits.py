# https://leetcode.com/problems/add-digits/

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0

# --------------- Runtime 33 ms, beats 66.63%. Memory 13.9MB, beats 39.79% ---------------


class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum(map(int, str(num)))

        return int(num)


# Alternative solution - recursion
# --------------- Runtime 35 ms, beats 55.39%. Memory 13.8MB, beats 90.82% ---------------

class Solution2:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num

        new_num = sum(map(int, str(num)))
        return self.addDigits(new_num)
