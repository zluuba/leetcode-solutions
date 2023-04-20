# https://leetcode.com/problems/strictly-palindromic-number/

# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive),
# the string representation of the integer n in base b is palindromic.

# Given an integer n, return true if n is strictly palindromic and false otherwise.
# A string is palindromic if it reads the same forward and backward.

# Example 1:
# Input: n = 9
# Output: false
# Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
# In base 3: 9 = 100 (base 3), which is not palindromic.
# Therefore, 9 is not strictly palindromic so we return false.
# Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.

# Example 2:
# Input: n = 4
# Output: false
# Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
# Therefore, we return false.

# --------------- Runtime 31 ms, beats 73.82%. Memory 14MB, beats 9.52% ---------------


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            current_base_num = []
            number = n
            while number > 0:
                current_base_num.append(number % base)
                number = number // base

            if current_base_num != current_base_num[::-1]:
                return False
        return True


# Alternative solution. Use numpy lib
# --------------- Runtime 78 ms, beats 5.7%. Memory 31.8MB, beats 9.52% ---------------
from numpy import base_repr


class Solution2:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            current_base_num = str(base_repr(n, base=i))
            if str(current_base_num) != str(current_base_num)[::-1]:
                return False
        return True
