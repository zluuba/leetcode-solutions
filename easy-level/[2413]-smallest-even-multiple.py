# https://leetcode.com/problems/smallest-even-multiple/

# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

# Example 1:
# Input: n = 5
# Output: 10
# Explanation: The smallest multiple of both 5 and 2 is 10.

# Example 2:
# Input: n = 6
# Output: 6
# Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.

# --------------- Runtime 47 ms, beats 55.26%. Memory 14.9MB, beats 77.47% ---------------


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n * 2


# Alternative solution. Less runtime, takes less memory
# --------------- Runtime 25 ms, beats 93.85%. Memory 13.7MB, beats 91.53% ---------------


class Solution2:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n << 1
