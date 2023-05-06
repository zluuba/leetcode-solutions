# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

# You are given an array of integers nums and an integer target.
# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is
# less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

# Example 1:
# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)

# Example 2:
# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

# Example 3:
# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).

# --------------- Runtime 7931 ms, beats 52.68%. Memory 27.9MB, beats 16.11% ---------------
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                result += pow(2, right - left)
                left += 1
            else:
                right -= 1

        return result % (10 ** 9 + 7)


# Alternative solution
# --------------- Runtime 7917 ms, beats 52.94%. Memory 29.1MB, beats 11.51% ---------------

class Solution2:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        length = len(nums)

        result = 0
        right = length - 1

        for i in range(length):
            while i <= right and nums[i] + nums[right] > target:
                right -= 1

            if i <= right:
                result += 2 ** (right - i)

        return result % (10 ** 9 + 7)
