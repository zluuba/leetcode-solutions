# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

# --------------- Runtime 43 ms, beats 96%. Memory 14.5MB, beats 98.31% ---------------
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for ind, num in enumerate(nums):
            if num >= target:
                return ind

        return len(nums)
