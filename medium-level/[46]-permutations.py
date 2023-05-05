# https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

# --------------- Runtime 60 ms, beats 5.14%. Memory 16.5MB, beats 7.37% ---------------
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(num)

            result.extend(perms)
            nums.append(num)

        return result
