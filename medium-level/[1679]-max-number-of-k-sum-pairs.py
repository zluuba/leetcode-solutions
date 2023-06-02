# https://leetcode.com/problems/max-number-of-k-sum-pairs/

# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

# --------------- Runtime 676 ms, beats 34.85%. Memory 28.5MB, beats 80.32% ---------------
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        p1, p2 = 0, len(nums) - 1

        nums.sort()

        while p1 < p2:
            if nums[p1] + nums[p2] == k:
                counter += 1
                p1 += 1
                p2 -= 1
            elif nums[p1] + nums[p2] > k:
                p2 -= 1
            elif nums[p1] + nums[p2] < k:
                p1 += 1

        return counter
