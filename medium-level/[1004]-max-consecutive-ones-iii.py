# https://leetcode.com/problems/max-consecutive-ones-iii/

# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# --------------- Runtime 61 ms, beats 84.66%. Memory 15.2MB, beats 41.36% ---------------
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        queue = []
        result = 0
        left = 0

        for right in range(length):
            if nums[right] == 0:
                queue.append(right)
            if len(queue) > k:
                result = max(result, right - left)
                left = queue.pop(0) + 1

        return max(result, length - left)
