# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray
# with value of 1's is [1,1,1,1,1].

# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

# --------------- Runtime 398 ms, beats 44.63%. Memory 18.9MB, beats 71.60% ---------------
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0

        if length == 1:
            return result

        left, right = 0, 1
        subarr = nums[left]
        subarr_len = 1

        while right < length:
            subarr += nums[right]
            subarr_len += 1

            if subarr in (subarr_len, subarr_len - 1):
                result = max(result, subarr_len - 1)
            else:
                subarr -= nums[left]
                left += 1
                subarr_len -= 1

            right += 1

        return result
