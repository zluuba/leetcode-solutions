# Given a positive integer n, find the pivot integer x such that:
#
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be
# at most one pivot index for the given input.

# Example:
# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

# --------------- Runtime 1325 ms, beats 11.48%. Memory 13.9MB, beats 48.56% ---------------


class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n + 1):
            if sum(range(1, i + 1)) == sum(range(i, n + 1)):
                return i
        return -1
