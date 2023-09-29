# https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
# 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
# 2 is the missing number in the range since it does not appear in nums.

# --------------- Runtime 120 ms, beats 79.65%. Memory 17.5MB, beats 98.97% ---------------
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target_sum = sum(range(len(nums) + 1))
        current_sum = sum(nums)

        return target_sum - current_sum


# Alternative solution - brute force
# --------------- Runtime 1494 ms, beats 12.65%. Memory 17.6MB, beats 92.25% ---------------

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(len(nums) + 1):
            if num not in nums:
                return num
