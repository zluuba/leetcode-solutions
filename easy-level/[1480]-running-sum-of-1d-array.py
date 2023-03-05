# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

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
