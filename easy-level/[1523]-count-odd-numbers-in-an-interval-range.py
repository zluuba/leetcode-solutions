# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# P.S. in this problem Constraints between 0 <= low <= high <= 10^9 and usual algorithms works too slow.

# --------------- Runtime 37 ms, beats 32.78%. Memory 13.9MB, beats 50.4% ---------------


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 0 and low % 2 == 0:
            return (high - low) // 2
        return (high - low) // 2 + 1
