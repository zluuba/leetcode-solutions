# https://leetcode.com/problems/find-pivot-index/

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the
# index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# --------------- Runtime 148 ms, beats 90.6%. Memory 15.3MB, beats 8.25% ---------------
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for ind, num in enumerate(nums):
            right -= num
            if left == right:
                return ind
            left += num
        return -1


# Alternative solution. More runtime, less memory usage
# --------------- Runtime 8768 ms, beats 5.9%. Memory 15.2MB, beats 87.15% ---------------


class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i + 1:] if i != len(nums) else 0

            if sum(left) == sum(right):
                return i
        return -1
