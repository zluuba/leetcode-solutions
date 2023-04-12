# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

# Example:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# --------------- Runtime 214 ms, beats 82.57%. Memory 16.2MB, beats 77.25% ---------------
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num ** 2 for num in nums])
