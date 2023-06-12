# https://leetcode.com/problems/summary-ranges/

# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:
#    -  "a->b" if a != b
#    -  "a" if a == b

# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

# Example 2:
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

# --------------- Runtime 44 ms, beats 54.77%. Memory 16.2MB, beats 64.73% ---------------
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        length = len(nums)
        left, right = 0, 0

        while right < length:
            if right + 1 < length:
                if nums[right + 1] == nums[right] + 1:
                    right += 1
                else:
                    result.append(
                        str(nums[left]) if left == right else
                        f'{nums[left]}->{nums[right]}'
                    )
                    right += 1
                    left = right
            else:
                result.append(
                    str(nums[left]) if nums[left] == nums[-1] else
                    f'{nums[left]}->{nums[-1]}'
                )
                break

        return result
