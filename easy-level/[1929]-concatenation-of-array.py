# Given an integer array nums of length n, you want to create an array ans
# of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.

# --------------- Runtime 86 ms, beats 81.57%. Memory 14.1MB, beats 94.45% ---------------


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums * 2
