# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).

# Example:
# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value,
# that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

# --------------- Runtime 61 ms, beats 22.36%. Memory 13.8MB, beats 98.73% ---------------
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_num1, max_num2 = nums[:2]

        return (max_num1 - 1) * (max_num2 - 1)