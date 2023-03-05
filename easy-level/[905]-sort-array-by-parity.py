# Given an integer array nums, move all the even integers at the beginning of the array
# followed by all the odd integers.
#
# Return any array that satisfies this condition.

# --------------- Runtime 78 ms, beats 86.74%. Memory 14.6MB, beats 94.65% ---------------
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda num: num % 2 != 0)
        return nums
