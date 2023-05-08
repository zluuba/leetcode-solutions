# https://leetcode.com/problems/longest-increasing-subsequence/

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# --------------- Runtime 75 ms, beats 88.1%. Memory 16.8MB, beats 7.61% ---------------
from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        lis = 1

        for i in range(1, len(nums)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                lis += 1
            else:
                index = bisect.bisect_left(temp, nums[i])
                temp[index] = nums[i]

        return lis


# Alternative solution
# --------------- Runtime 3808 ms, beats 11.27%. Memory 16.7MB, beats 13.51% ---------------

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        lis = [1] * length

        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)
