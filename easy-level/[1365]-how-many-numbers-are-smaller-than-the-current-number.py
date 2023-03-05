# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
#
# Return the answer in an array.

# --------------- Runtime 371 ms, beats 33.20%. Memory 13.8MB, beats 79.67% ---------------
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            count = [1 if i > x else 0 for x in nums if i != x]
            result.append(sum(count))
        return result
