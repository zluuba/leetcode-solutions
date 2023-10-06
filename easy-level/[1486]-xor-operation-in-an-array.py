# https://leetcode.com/problems/xor-operation-in-an-array/

# You are given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

# Example 1:
# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.

# Example 2:
# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.

# --------------- Runtime 39 ms, beats 52.68%. Memory 16.2MB, beats 82.88% ---------------

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0

        for i in range(n):
            result ^= start + 2 * i

        return result


# Alternative solution - using reduce() func
# --------------- Runtime 45 ms, beats 15.47%. Memory 16.1MB, beats 82.88% ---------------
from functools import reduce


class Solution2:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]

        return reduce(
            lambda num1, num2: num1 ^ num2,
            nums,
            0,
        )
