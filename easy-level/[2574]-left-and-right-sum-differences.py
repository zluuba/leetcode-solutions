# https://leetcode.com/problems/left-and-right-sum-differences/

# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
# - answer.length == nums.length.
# - answer[i] = |leftSum[i] - rightSum[i]|.

# Where:
# - leftSum[i] is the sum of elements to the left of the index i in the array nums.
#   If there is no such element, leftSum[i] = 0.
# - rightSum[i] is the sum of elements to the right of the index i in the array nums.
#   If there is no such element, rightSum[i] = 0.

# Return the array answer.

# Example 1:
# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

# Example 2:
# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].

# --------------- Runtime 71 ms, beats 84.56%. Memory 14.1MB, beats 54.33% ---------------
from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        result = []
        left_sum, right_sum = 0, sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]
            result.append(abs(right_sum - left_sum))
            left_sum += nums[i]

        return result
