# https://leetcode.com/problems/sum-of-digits-in-base-k/

# Given an integer n (in base 10) and a base k,
# return the sum of the digits of n after converting n from base 10 to base k.
# After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.

# Example 1:
# Input: n = 34, k = 6
# Output: 9
# Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

# Example 2:
# Input: n = 10, k = 10
# Output: 1
# Explanation: n is already in base 10. 1 + 0 = 1.

# --------------- Runtime 36 ms, beats 59.84%. Memory 16.3MB, beats 30.74% ---------------


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digits = []

        while n > 0:
            digits.append(n % k)
            n = n // k

        return sum(digits)


# Alternative solution - longest
# --------------- Runtime 35 ms, beats 64.34%. Memory 16.2MB, beats 30.74% ---------------

class Solution2:
    def num_to_base(self, num, base):
        result = ''
        while num > 0:
            result = str(num % base) + result
            num = num // base

        return int(result)

    def sumBase(self, n: int, k: int) -> int:
        num_base_k = self.num_to_base(n, k)
        return sum(map(int, str(num_base_k)))
