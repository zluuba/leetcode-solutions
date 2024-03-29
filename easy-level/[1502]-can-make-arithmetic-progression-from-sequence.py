# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# A sequence of numbers is called an arithmetic progression if the difference
# between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
# Otherwise, return false.

# Example 1:
# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively,
# between each consecutive elements.

# Example 2:
# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

# --------------- Runtime 43 ms, beats 77.83%. Memory 16.5MB, beats 20.83% ---------------
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort(reverse=True)
        diff = arr[0] - arr[1]

        for i in range(2, len(arr), 2):
            prev = arr[i - 1]
            curr = arr[i]

            if prev - curr != diff:
                return False

        return True
