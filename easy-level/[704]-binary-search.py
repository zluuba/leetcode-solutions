# https://leetcode.com/problems/binary-search/

# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# --------------- Runtime 230 ms, beats 98.48%. Memory 15.5MB, beats 16.43% ---------------
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1, p2 = 0, len(nums) - 1

        while p1 <= p2:
            middle = (p1 + p2) // 2

            if nums[middle] < target:
                p1 = middle + 1
            elif nums[middle] > target:
                p2 = middle - 1
            else:
                return middle

        return -1
