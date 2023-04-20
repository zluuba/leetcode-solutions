# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
# P.S. in this problem Constraints between 0 <= low <= high <= 10^9 and usual algorithms works too slow.

# Example 1:
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].

# --------------- Runtime 37 ms, beats 32.78%. Memory 13.9MB, beats 50.4% ---------------


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 0 and low % 2 == 0:
            return (high - low) // 2
        return (high - low) // 2 + 1
