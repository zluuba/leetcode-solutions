# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# --------------- Runtime 2895 ms, beats 9.11%. Memory 13.7MB, beats 99.89% ---------------


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 2 or x == 3:
            return 1

        floor = 0
        for num in range(0, x):
            if num * num == x:
                return num
            elif num * num < x:
                floor = num
            else:
                return floor

        return x
