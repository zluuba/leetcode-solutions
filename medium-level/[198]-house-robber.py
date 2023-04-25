# https://leetcode.com/problems/house-robber/

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
# adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# --------------- Runtime 36 ms, beats 40.56%. Memory 13.8MB, beats 94.86% ---------------
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0, 0

        for curr_house in nums:
            house1, house2 = house2, max(house1 + curr_house, house2)

        return house2


# Alternative solution
# --------------- Runtime 40 ms, beats 13.60%. Memory 14MB, beats 11.95% ---------------

class Solution2:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return max(nums)

        dp = [0] * length
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, length):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
