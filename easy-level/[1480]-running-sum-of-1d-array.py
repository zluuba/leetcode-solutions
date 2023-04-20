# https://leetcode.com/problems/running-sum-of-1d-array/

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

# --------------- Runtime 41 ms, beats 73.85%. Memory 14.1MB, beats 67.37% ---------------
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return nums

        result = [nums[0]]
        for ind, num in enumerate(nums[1:]):
            result.append(num + result[ind])
        return result
