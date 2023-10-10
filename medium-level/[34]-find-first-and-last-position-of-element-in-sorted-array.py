# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# --------------- Runtime 85 ms, beats 51.33%. Memory 17.7MB, beats 84.38% ---------------
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for ind in range(length):
            curr = nums[ind]

            if curr == target:
                start = ind

                while ind < length and nums[ind] == nums[start]:
                    ind += 1

                return [start, ind - 1]

            elif curr > target:
                break

        return [-1, -1]
