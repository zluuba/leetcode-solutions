# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.

# --------------- Runtime 664 ms, beats 53.87%. Memory 27.9MB, beats 88.62% ---------------
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p1 = p2 = 0
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break

        tmp = 0
        while True:
            p1 = nums[p1]
            tmp = nums[tmp]
            if p1 == tmp:
                return tmp
