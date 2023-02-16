# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

# --------------- Runtime 59 ms, beats 29.7%. Memory 14.6MB, beats 74.20% ---------------


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)
