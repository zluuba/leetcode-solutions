# https://leetcode.com/problems/range-sum-query-immutable/

# Given an integer array nums, handle multiple queries of the following type:
#  - Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#  - NumArray(int[] nums) Initializes the object with the integer array nums.
#  - int sumRange(int left, int right) Returns the sum of the elements of nums
#    between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

# Example:
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

# --------------- Runtime 75 ms, beats 75.37%. Memory 19.9MB, beats 73.10% ---------------
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [nums[0]]

        for i in range(1, len(nums)):
            self.sums.append(self.sums[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] if not left else self.sums[right] - self.sums[left - 1]


# Alternative solution - no optimization
# --------------- Runtime 1024 ms, beats 17.53%. Memory 19.7MB, beats 86.65% ---------------

class NumArray2:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        chunk = self.nums[left: right + 1]
        return sum(chunk)
