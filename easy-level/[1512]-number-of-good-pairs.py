# https://leetcode.com/problems/number-of-good-pairs/

# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0

# --------------- Runtime 38 ms, beats 57.67%. Memory 13.8MB, beats 48.73% ---------------
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        length = len(nums)
        counter = 0
        for i in range(0, length - 1):
            for j in range(i, length):
                if nums[i] == nums[j] and i < j:
                    counter += 1
        return counter
