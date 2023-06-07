# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

# Given 3 positives numbers a, b and c.
# Return the minimum flips required in some bits of a and b to make ( a OR b == c ) (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

# Example 1:
# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

# Example 2:
# Input: a = 4, b = 2, c = 7
# Output: 1

# Example 3:
# Input: a = 1, b = 2, c = 3
# Output: 0

# --------------- Runtime 40 ms, beats 77.80%. Memory 16.3MB, beats 68.57% ---------------

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if bin(a | b) == bin(c):
            return 0

        result = 0

        while a > 0 or b > 0 or c > 0:
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1

            if bit_c == 0:
                result += (bit_a + bit_b)
            else:
                result += 1 if (bit_a == bit_b == 0) else 0

            a, b, c = a >> 1, b >> 1, c >> 1

        return result
