# https://leetcode.com/problems/monotonic-array/

# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
#     An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example 1:
# Input: nums = [1,2,2,3]
# Output: true

# Example 2:
# Input: nums = [6,5,4,4]
# Output: true

# Example 3:
# Input: nums = [1,3,2]
# Output: false

# --------------- Runtime 827 ms, beats 63.7%. Memory 30.4MB, beats 95.58% ---------------
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff = 0

        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i - 1]

            if (diff > 0 > curr_diff) or (diff < 0 < curr_diff):
                return False
            if curr_diff:
                diff = curr_diff

        return True


# Alternative solution - lazy
# --------------- Runtime 896 ms, beats 7.46%. Memory 30.9MB, beats 13.51% ---------------

class Solution2:
    def isMonotonic(self, nums: List[int]) -> bool:
        return (nums == sorted(nums)) or (nums == sorted(nums, reverse=True))
