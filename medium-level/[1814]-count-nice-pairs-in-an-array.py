# https://leetcode.com/problems/count-nice-pairs-in-an-array/

# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of
# the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21.
# A pair of indices (i, j) is nice if it satisfies all of the following conditions:
#  - 0 <= i < j < nums.length
#  - nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

# Example 1:
# Input: nums = [42,11,1,97]
# Output: 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

# Example 2:
# Input: nums = [13,10,35,24,76]
# Output: 4

# --------------- Runtime 585 ms, beats 60.34%. Memory 26.8MB, beats 61.19% ---------------
from typing import List


class Solution:
    @staticmethod
    def reverse_number(number):
        return int(str(number)[::-1])

    def countNicePairs(self, nums: List[int]) -> int:
        pairs = dict()
        nice_pairs_count = 0

        for num in nums:
            num -= self.reverse_number(num)

            if num in pairs:
                nice_pairs_count += pairs[num]

            pairs[num] = pairs.get(num, 0) + 1

        return nice_pairs_count % (10 ** 9 + 7)
