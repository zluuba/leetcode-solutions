# https://leetcode.com/problems/find-unique-binary-string/

# Given an array of strings nums containing n unique binary strings each of length n,
# return a binary string of length n that does not appear in nums.
# If there are multiple answers, you may return any of them.

# Example 1:
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.

# Example 2:
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.

# Example 3:
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

# --------------- Runtime 47 ms, beats 31.34%. Memory 16.2MB, beats 66.27% ---------------
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)

        start = int('0' * length, 2)
        end = int('1' * length, 2)

        for num in range(start, end + 1):
            bin_num = (bin(num)[2:]).rjust(length, '0')

            if bin_num not in nums:
                return bin_num
