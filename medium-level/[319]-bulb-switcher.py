# https://leetcode.com/problems/bulb-switcher/

# There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
# For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
# Return the number of bulbs that are on after n rounds.

# Example 1:
# Input: n = 3
# Output: 1
# Explanation: At first, the three bulbs are [off, off, off].
# After the first round, the three bulbs are [on, on, on].
# After the second round, the three bulbs are [on, off, on].
# After the third round, the three bulbs are [on, off, off].
# So you should return 1 because there is only one bulb is on.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 1

# --------------- Runtime 55 ms, beats 8.42%. Memory 16.2MB, beats 34.9% ---------------
# The problem is solved by finding the number of perfect squares: 1 * 1, 2 * 2, 3 * 3, etc


class Solution:
    def bulbSwitch(self, n: int) -> int:
        perf_squares = 0
        while True:
            perf_squares += 1
            if perf_squares ** 2 > n:
                return perf_squares - 1


# Alternative solution
# --------------- Runtime 37 ms, beats 17.4%. Memory 16.3MB, beats 34.9% ---------------
from math import sqrt


class Solution2:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))
