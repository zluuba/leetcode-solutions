# https://leetcode.com/problems/new-21-game/

# Alice plays the following game, loosely based on the card game "21".
# Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an
# integer number of points randomly from the range [1, maxPts], where maxPts is an integer.
# Each draw is independent and the outcomes have equal probabilities.
# Alice stops drawing numbers when she gets k or more points.
# Return the probability that Alice has n or fewer points.
# Answers within 10-5 of the actual answer are considered accepted.

# Example 1:
# Input: n = 10, k = 1, maxPts = 10
# Output: 1.00000
# Explanation: Alice gets a single card, then stops.

# Example 2:
# Input: n = 6, k = 1, maxPts = 10
# Output: 0.60000
# Explanation: Alice gets a single card, then stops.
# In 6 out of 10 possibilities, she is at or below 6 points.

# Example 3:
# Input: n = 21, k = 17, maxPts = 10
# Output: 0.73278

# --------------- Runtime 106 ms, beats 26.27%. Memory 17.2MB, beats 5.93% ---------------


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0

        window_sum = 0
        for i in range(k, k + maxPts):
            if i <= n:
                window_sum += 1

        dp = {}
        for i in range(k - 1, -1, -1):
            dp[i] = window_sum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)

            window_sum += dp[i] - remove

        return dp[0]
