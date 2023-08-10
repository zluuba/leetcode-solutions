# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# --------------- Runtime 36 ms, beats 93.18%. Memory 16.4MB, beats 32.17% ---------------

class Solution:
    def reverse(self, x: int) -> int:
        min_value, max_value = (-2 ** 31, 2 ** 31 - 1)
        str_num = str(x)
        sign = '+'

        if str_num[0] == '-':
            sign = '-'
            str_num = str_num[1:]

        new_num = int(sign + str_num[::-1])

        return new_num if (min_value < new_num < max_value) else 0
