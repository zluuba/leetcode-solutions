# https://leetcode.com/problems/sort-array-by-parity/

# Given an integer array nums, move all the even integers at the beginning of the array
# followed by all the odd integers.

# Return any array that satisfies this condition.

# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:
# Input: nums = [0]
# Output: [0]

# --------------- Runtime 78 ms, beats 86.74%. Memory 14.6MB, beats 94.65% ---------------
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda num: num % 2 != 0)
        return nums


# Alternative solution - list comprehension: fast, but fat
# --------------- Runtime 70 ms, beats 88.10%. Memory 17MB, beats 96.40% ---------------

class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_nums = [num for num in nums if num % 2 == 0]
        odd_nums = [num for num in nums if num % 2 != 0]

        return even_nums + odd_nums
