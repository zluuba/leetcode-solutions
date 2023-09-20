# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

# You are given a 0-indexed integer array nums and an integer k.
# Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in
# their binary representation.
# The set bits in an integer are the 1's present when it is written in binary.
#  - For example, the binary representation of 21 is 10101, which has 3 set bits.

# Example:
# Input: nums = [5,10,1,5,2], k = 1
# Output: 13
# Explanation: The binary representation of the indices are:
# 0 = 0002
# 1 = 0012
# 2 = 0102
# 3 = 0112
# 4 = 1002
# Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
# Hence, the answer is nums[1] + nums[2] + nums[4] = 13.

# --------------- Runtime 80 ms, beats 63.59%. Memory 16.4MB, beats 48.77% ---------------
from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(val for ind, val in enumerate(nums) if bin(ind).count('1') == k)


# Alternative solution - no .count() method
# --------------- Runtime 101 ms, beats 11.59%. Memory 16.3MB, beats 77.12% ---------------

class Solution2:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0

        for ind, val in enumerate(nums):
            bin_ind = bin(ind)[2:]
            bin_sum = sum(map(int, bin_ind))

            if bin_sum == k:
                result += val

        return result
