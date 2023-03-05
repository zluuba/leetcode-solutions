# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.

# --------------- Runtime 155 ms, beats 99.78%. Memory 23.6MB, beats 99.62% ---------------
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        p1, p2 = 0, len(nums) - 1

        while p1 < p2:
            mid = (p1 + p2) // 2

            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                p2 = mid
            else:
                p1 = mid + 2

        return nums[p1]
