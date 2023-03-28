# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
#
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
#
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

# Example:
# Input: s = "a1b2c3d4e"
# Output: "abbdcfdhe"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('b',2) = 'd'
# - s[5] -> shift('c',3) = 'f'
# - s[7] -> shift('d',4) = 'h'

# --------------- Runtime 29 ms, beats 81.4%. Memory 13.8MB, beats 93.51% ---------------


class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ''

        for char in s:
            if char.isdigit():
                prev_char = result[-1]
                char = chr(ord(prev_char) + int(char))
            result += char

        return result
