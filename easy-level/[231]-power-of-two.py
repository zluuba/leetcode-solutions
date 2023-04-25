# https://leetcode.com/problems/power-of-two/

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16

# Example 3:
# Input: n = 3
# Output: false

# --------------- Runtime 38 ms, beats 34.11%. Memory 13.8MB, beats 89.88% ---------------


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        curr = 0

        while curr <= n:
            curr = 2 ** power
            if curr == n:
                return True
            power += 1

        return False


# Alternative solution - recursion
# --------------- Runtime 36 ms, beats 43.47%. Memory 13.8MB, beats 89.88% ---------------

class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n in {1, 2}:
            return True
        elif n < 1:
            return False

        return self.isPowerOfTwo(n / 2)


# Alternative solution - binary counting
# --------------- Runtime 34 ms, beats 61.85%. Memory 13.7MB, beats 89.88% ---------------

class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return bin(n).count('1') == 1
