# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# --------------- Runtime 5956 ms, beats 9.57%. Memory 16.7MB, beats 45.77% ---------------
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num


# Alternative solution. Lowest runtime
# --------------- Runtime 138 ms, beats 70.3%. Memory 17.1MB, beats 10.12% ---------------


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
