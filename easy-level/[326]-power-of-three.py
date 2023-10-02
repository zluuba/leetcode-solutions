# https://leetcode.com/problems/power-of-three/

# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).

# --------------- Runtime 71 ms, beats 70.52%. Memory 16MB, beats 98.44% ---------------

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n /= 3

        return n == 1


# Alternative solution - overhead multiply
# --------------- Runtime 83 ms, beats 34.68%. Memory 16.3MB, beats 27.84% ---------------

class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        curr = 1

        while curr <= n:
            if curr == n:
                return True

            curr *= 3

        return False
