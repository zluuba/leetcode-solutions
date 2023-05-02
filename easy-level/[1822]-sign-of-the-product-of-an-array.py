# https://leetcode.com/problems/sign-of-the-product-of-an-array/

# There is a function signFunc(x) that returns:
# - 1 if x is positive.
# - -1 if x is negative.
# - 0 if x is equal to 0.

# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).

# Example 1:
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1

# Example 2:
# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0

# Example 3:
# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

# --------------- Runtime 69 ms, beats 16.83%. Memory 16.4MB, beats 7.53% ---------------
from typing import List
from functools import reduce


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        signFunc = lambda num: 1 if num > 0 else (-1 if num < 0 else 0)

        product = reduce(lambda x, y: x * y, nums)
        return signFunc(product)


# Alternative solution - without signFunc
# --------------- Runtime 72 ms, beats 8.89%. Memory 16.5MB, beats 7.53% ---------------

class Solution2:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0

        negatives = [num for num in nums if num < 0]

        if len(negatives) % 2 == 0:
            return 1
        return -1
