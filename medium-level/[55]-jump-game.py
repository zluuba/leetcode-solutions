# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.

# --------------- Runtime 519 ms, beats 51.40%. Memory 15.2MB, beats 78.83% ---------------
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0

        for index, number in enumerate(nums):
            if curr >= index:
                curr = max(curr, index + number)
                continue
            return False
        return True
