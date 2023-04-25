# https://leetcode.com/problems/reverse-bits/

# Reverse bits of a given 32 bits unsigned integer.

# Example 1:
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
# so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
# so return 3221225471 which its binary representation is 10111111111111111111111111111111.

# --------------- Runtime 33 ms, beats 66.96%. Memory 13.8MB, beats 87.14% ---------------


class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = binary.rjust(32, '0')

        return int(binary[::-1], 2)
