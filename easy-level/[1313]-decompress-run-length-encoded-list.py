# We are given a list nums of integers representing a list compressed with run-length encoding.
#
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
# For each such pair, there are freq elements with value val concatenated in a sublist.
# Concatenate all the sublists from left to right to generate the decompressed list.
#
# Return the decompressed list.

# --------------- Runtime 65 ms, beats 87.43%. Memory 14.5MB, beats 22.35% ---------------
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for ind in range(0, len(nums) - 1, 2):
            count, num = nums[ind], nums[ind + 1]
            result.extend([num] * count)

        return result
