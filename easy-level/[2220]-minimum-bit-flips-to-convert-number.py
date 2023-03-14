# A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either
# 0 to 1 or 1 to 0.

# For example, for x = 7, the binary representation is 111 and we may choose any bit
# (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110,
# flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
# Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

# Example:
# Input: start = 10, goal = 7
# Output: 3
# Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
# - Flip the first bit from the right: 1010 -> 1011.
# - Flip the third bit from the right: 1011 -> 1111.
# - Flip the fourth bit from the right: 1111 -> 0111.
# It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

# --------------- Runtime 25 ms, beats 95.32%. Memory 13.8MB, beats 95.99% ---------------


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_start = bin(start).lstrip('0b')
        bin_goal = bin(goal).lstrip('0b')

        length_diff = len(bin_start) - len(bin_goal)
        if length_diff < 0:
            bin_start = ('0' * abs(length_diff)) + bin_start
        elif length_diff > 0:
            bin_goal = ('0' * length_diff) + bin_goal

        flips = [1 for i in range(len(bin_start)) if bin_start[i] != bin_goal[i]]
        return sum(flips)
