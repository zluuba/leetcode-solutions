# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1].
# The test cases are generated such that you can reach nums[n - 1].

# --------------- Runtime 124 ms, beats 93.23%. Memory 15MB, beats 54.98% ---------------
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        left_border = 0
        right_border = 0

        if len(nums) == 1:
            return steps

        while left_border < len(nums) - 1:
            bigger_step = 0
            for i in range(right_border, left_border + 1):
                if bigger_step < i + nums[i]:
                    bigger_step = i + nums[i]
            right_border = left_border + 1
            left_border = bigger_step
            steps += 1

        return steps
