# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

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
