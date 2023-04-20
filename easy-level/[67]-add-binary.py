# https://leetcode.com/problems/add-binary/

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Short solution
# --------------- Runtime 38 ms, beats 53.43%. Memory 13.8MB, beats 63.5% ---------------


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        summ = int(a, 2) + int(b, 2)
        bin_sum = bin(summ)
        return bin_sum[2:]


# Long solution without bin function
# --------------- Runtime 35 ms, beats 69.29%. Memory 13.9MB, beats 63.5% ---------------


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        zero = '0'
        one = '1'

        if len(a) > len(b):
            b = zero * (len(a) - len(b)) + b
        else:
            a = zero * (len(b) - len(a)) + a

        result = ''
        rem = 0
        for i in range(len(a) - 1, -1, -1):
            if a[i] == b[i]:
                result += zero if rem == 0 else one
                rem = 0 if a[i] == zero else 1

            else:
                result += one if rem == 0 else zero

            if i == 0 and rem == 1:
                result += one

        return result[::-1]
