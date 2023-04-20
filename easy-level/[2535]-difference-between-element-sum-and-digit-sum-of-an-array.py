# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

# You are given a positive integer array nums.
# - The element sum is the sum of all the elements in nums.
# - The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.

# Return the absolute difference between the element sum and digit sum of nums.
# Note that the absolute difference between two integers x and y is defined as |x - y|.

# Example 1:
# Input: nums = [1,15,6,3]
# Output: 9
# Explanation:
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 0
# Explanation:
# The element sum of nums is 1 + 2 + 3 + 4 = 10.
# The digit sum of nums is 1 + 2 + 3 + 4 = 10.
# The absolute difference between the element sum and digit sum is |10 - 10| = 0.

# --------------- Runtime 159 ms, beats 30.33%. Memory 14MB, beats 90.90% ---------------
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            digs = str(num)
            for char in digs:
                digit_sum += int(char)

        return abs(elem_sum - digit_sum)


# Alternative solution
# --------------- Runtime 129 ms, beats 85.18%. Memory 14.2MB, beats 53.11% ---------------


class Solution2:
    def differenceOfSum(self, nums: List[int]) -> int:
        digits = ''.join([str(n) for n in nums])
        digit_sum = sum(list(map(int, digits)))
        return abs(sum(nums) - digit_sum)
