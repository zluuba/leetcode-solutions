# Given an integer array nums, move all the even integers at the beginning of the array
# followed by all the odd integers.
#
# Return any array that satisfies this condition.

# --------------- Runtime 78 ms, beats 86.74%. Memory 14.6MB, beats 94.65% ---------------


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        nums.sort(key=lambda num: num % 2 != 0)
        return nums
