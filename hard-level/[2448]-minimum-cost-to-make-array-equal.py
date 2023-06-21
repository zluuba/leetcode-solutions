# https://leetcode.com/problems/minimum-cost-to-make-array-equal/

# You are given two 0-indexed arrays nums and cost consisting each of n positive integers.
# You can do the following operation any number of times:
# - Increase or decrease any element of the array nums by 1.

# The cost of doing one operation on the ith element is cost[i].
# Return the minimum total cost such that all the elements of the array nums become equal.

# Example 1:
# Input: nums = [1,3,5,2], cost = [2,3,1,14]
# Output: 8
# Explanation: We can make all the elements equal to 2 in the following way:
# - Increase the 0th element one time. The cost is 2.
# - Decrease the 1st element one time. The cost is 3.
# - Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
# The total cost is 2 + 3 + 3 = 8.
# It can be shown that we cannot make the array equal with a smaller cost.

# Example 2:
# Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
# Output: 0
# Explanation: All the elements are already equal, so no operations are needed.

# --------------- Runtime 1035 ms, beats 23.53%. Memory 32MB, beats 52.94% ---------------
from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        length = len(nums)
        lower = min(nums)
        higher = max(nums)

        get_total_cost = lambda num: sum(abs(nums[i] - num) * cost[i] for i in range(length))

        while higher - lower > 1:
            middle = (lower + higher) // 2

            if get_total_cost(middle) <= get_total_cost(middle + 1):
                higher = middle
            else:
                lower = middle + 1

        return min(get_total_cost(lower), get_total_cost(higher))
