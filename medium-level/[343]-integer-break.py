# https://leetcode.com/problems/integer-break/

# Given an integer n, break it into the sum of k positive integers, where k >= 2,
# and maximize the product of those integers.
# Return the maximum product you can get.

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

# --------------- Runtime 33 ms, beats 90.84%. Memory 16.2MB, beats 85.57% ---------------

class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1

        result, curr = 1, n

        while curr > 4:
            result *= 3
            curr -= 3

        result *= curr
        return result
