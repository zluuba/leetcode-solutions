# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
#  - For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be
#    max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
#  - Each element of nums is in exactly one pair, and
#  - The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.

# Example 1:
# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

# Example 2:
# Input: nums = [3,5,4,2,4,6]
# Output: 8
# Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
# The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.

# --------------- Runtime 985 ms, beats 59.10%. Memory 30.2MB, beats 87.41% ---------------
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        pair_sums = [nums[left] + nums[length - left - 1] for left in range(length // 2)]

        return max(pair_sums)


# Alternative solution - pointers
# --------------- Runtime 975 ms, beats 74.42%. Memory 31MB, beats 7.66% ---------------

class Solution2:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum = 0

        left, right = 0, len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]
            max_pair_sum = max(max_pair_sum, curr_sum)

            left += 1
            right -= 1

        return max_pair_sum
