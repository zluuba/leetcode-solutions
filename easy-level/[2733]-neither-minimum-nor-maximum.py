# https://leetcode.com/problems/neither-minimum-nor-maximum/

# Given an integer array nums containing distinct positive integers,
# find and return any number from the array that is neither the minimum nor the maximum value in the array,
# or -1 if there is no such number.
# Return the selected integer.

# Example 1:
# Input: nums = [3,2,1,4]
# Output: 2
# Explanation: In this example, the minimum value is 1 and the maximum value is 4.
# Therefore, either 2 or 3 can be valid answers.

# Example 2:
# Input: nums = [1,2]
# Output: -1
# Explanation: Since there is no number in nums that is neither the maximum nor the minimum,
# we cannot select a number that satisfies the given condition. Therefore, there is no answer.

# Example 3:
# Input: nums = [2,1,3]
# Output: 2
# Explanation: Since 2 is neither the maximum nor the minimum value in nums, it is the only valid answer.

# --------------- Runtime 381 ms, beats 81.96%. Memory 16.2MB, beats 97.74% ---------------
from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        min_num, max_num = min(nums), max(nums)

        for num in nums:
            if num not in (min_num, max_num):
                return num


# Alternative solution - without min/max
# --------------- Runtime 391 ms, beats 55%. Memory 16.4MB, beats 7.27% ---------------

class Solution2:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums = sorted(nums)
        min_num, max_num = nums[0], nums[-1]

        for num in nums[1:]:
            if num not in (min_num, max_num):
                return num
        return -1
