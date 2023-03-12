# Given an integer array nums and an integer k, return the number of pairs (i, j)
# where i < j such that |nums[i] - nums[j]| == k.
#
# The value of |x| is defined as:
# x if x >= 0.
# -x if x < 0.

# Example:
# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]

# --------------- Runtime 222 ms, beats 45.80%. Memory 13.9MB, beats 55.84% ---------------
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        length = len(nums)
        result = 0

        for i in range(length):
            for j in range(i + 1, length):
                if abs(nums[i] - nums[j]) == k:
                    result += 1

        return result
