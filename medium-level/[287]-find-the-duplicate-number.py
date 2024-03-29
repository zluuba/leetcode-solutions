# https://leetcode.com/problems/find-the-duplicate-number/

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

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


# Alternative solution - just dict it
# --------------- Runtime 495 ms, beats 97.77%. Memory 34.9MB, beats 10.12% ---------------

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        dictionary = dict()

        for num in nums:
            if num in dictionary:
                return num

            dictionary[num] = 1

