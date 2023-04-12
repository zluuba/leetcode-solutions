# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# --------------- Runtime 216 ms, beats 75.56%. Memory 25.6MB, beats 6.35% ---------------
from typing import List


# Do not return anything, modify nums in-place instead.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        offset = length - (k % length)
        result = nums[offset:] + nums[:offset]
        nums.clear()
        nums.extend(result)


# --------------- Runtime 2097 ms, beats 15.70%. Memory 25.3MB, beats 72.62% ---------------


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        [nums.insert(0, nums.pop()) for _ in range(k)]
