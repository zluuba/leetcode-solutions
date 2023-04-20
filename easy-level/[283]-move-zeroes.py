# https://leetcode.com/problems/move-zeroes/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative
# order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# --------------- Runtime 152 ms, beats 98.98%. Memory 15.5MB, beats 50.80% ---------------
from typing import List


# Do not return anything, modify nums in-place instead.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = nums.count(0)

        nums[:] = [num for num in nums if num != 0]
        nums += [0] * zeros


# --------------- Runtime 991 ms, beats 14%. Memory 15.6MB, beats 50.80% ---------------
# Alternative solution without slicing

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = nums.count(0)

        while 0 in nums:
            nums.remove(0)
        nums.extend([0] * zeros)
