# https://leetcode.com/problems/maximum-average-subarray-i/description

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

# --------------- Runtime 1220 ms, beats 48.10%. Memory 28MB, beats 68.43% ---------------
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)

        if length == 1:
            return nums[0]
        if k >= length:
            return sum(nums) / k

        ind = 0
        sub_sum = sum(nums[ind:k])
        max_average = sub_sum / k

        while ind + k < length:
            sub_sum = sub_sum - nums[ind] + nums[ind + k]
            max_average = max(max_average, sub_sum / k)
            ind += 1

        return max_average
