# Given two integers num1 and num2, return the sum of the two integers.

# --------------- Runtime 30 ms, beats 80.57%. Memory 13.7MB, beats 93.89% ---------------


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return sum([num1, num2])


# Canonical solution. What could be easier?
# --------------- Runtime 39 ms, beats 32.21%. Memory 13.9MB, beats 45.1% ---------------


class Solution2:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
