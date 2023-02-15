# The array-form of an integer num is an array representing its digits in left to right order.
#
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

# --------------- Runtime 307 ms, beats 77.55%. Memory 15MB, beats 65.15% ---------------


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        s = int(''.join(map(str, num))) + k
        result = list(map(int, str(s)))
        return result
