# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

# You are given an integer array nums (0-indexed).
# In one operation, you can choose an element of the array and increment it by 1.
# For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
# Return the minimum number of operations needed to make nums strictly increasing.

# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
# An array of length 1 is trivially strictly increasing.

# Example 1:
# Input: nums = [1,1,1]
# Output: 3
# Explanation: You can do the following operations:
# 1) Increment nums[2], so nums becomes [1,1,2].
# 2) Increment nums[1], so nums becomes [1,2,2].
# 3) Increment nums[2], so nums becomes [1,2,3].

# Example 2:
# Input: nums = [1,5,2,4,1]
# Output: 14

# Example 3:
# Input: nums = [8]
# Output: 0

# --------------- Runtime 134 ms, beats 85.67%. Memory 17.2MB, beats 24.59% ---------------
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums) - 1):
            curr = nums[i]
            next = nums[i + 1]

            if curr >= next:
                nums[i + 1] = curr + 1
                result += curr - next + 1

        return result


# Alternative solution - without array changing
# --------------- Runtime 136 ms, beats 80.9%. Memory 17.1MB, beats 67.87% ---------------

class Solution2:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            if prev >= curr:
                result += prev + 1 - curr
                prev += 1
            else:
                prev = curr

        return result
