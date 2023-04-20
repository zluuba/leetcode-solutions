# https://leetcode.com/problems/plus-one/

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit
# of the integer. The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

# --------------- Runtime 39 ms, beats 39.62%. Memory 13.8MB, beats 95.28% ---------------
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(num) for num in digits])
        num_plus_one = int(num) + 1
        return [int(num) for num in str(num_plus_one)]


# Alternative solution. Without list comprehension
# --------------- Runtime 35 ms, beats 63.91%. Memory 13.8MB, beats 50.5% ---------------


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_ind = len(digits) - 1

        for ind in range(last_ind, -1, -1):
            if digits[ind] < 9:
                digits[ind] += 1
                return digits
            digits[ind] = 0

        return [1] + digits
