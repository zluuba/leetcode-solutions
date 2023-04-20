# https://leetcode.com/problems/add-two-integers/

# Given two integers num1 and num2, return the sum of the two integers.

# Example 1:
# Input: num1 = 12, num2 = 5
# Output: 17
# Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

# Example 2:
# Input: num1 = -10, num2 = 4
# Output: -6
# Explanation: num1 + num2 = -6, so -6 is returned.

# --------------- Runtime 30 ms, beats 80.57%. Memory 13.7MB, beats 93.89% ---------------


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return sum([num1, num2])


# Canonical solution. What could be easier?
# --------------- Runtime 39 ms, beats 32.21%. Memory 13.9MB, beats 45.1% ---------------


class Solution2:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
