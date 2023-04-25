# https://leetcode.com/problems/number-of-1-bits/

# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits
# it has (also known as the Hamming weight).
# Note:
# - Note that in some languages, such as Java, there is no unsigned integer type.
#   In this case, the input will be given as a signed integer type.
#   It should not affect your implementation, as the integer's internal binary representation is the same,
#   whether it is signed or unsigned.

# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Example 2:
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

# Example 3:
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

# --------------- Runtime 34 ms, beats 49.63%. Memory 13.7MB, beats 88.60% ---------------


class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(map(int, bin(n)[2:]))


# Alternative solution - simplest
# --------------- Runtime 36 ms, beats 37.50%. Memory 13.9MB, beats 36.67% ---------------

class Solution2:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
