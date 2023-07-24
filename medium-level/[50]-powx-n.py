# https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# --------------- Runtime 43 ms, beats 80.40%. Memory 16.2MB, beats 97.24% ---------------


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        return x * self.myPow(x, n - 1)
