# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# Example 1:
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15

# Example 2:
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21

# --------------- Runtime 32 ms, beats 57.2%. Memory 13.8MB, beats 92.68% ---------------
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))

        prod = reduce(lambda x, y: x * y, digits)
        s = sum(digits)

        return prod - s
