# Given two positive integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.

# Example:
# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

# --------------- Runtime 30 ms, beats 80.14%. Memory 13.8MB, beats 48.11% ---------------


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        cf_counter = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                cf_counter += 1

        return cf_counter


# List comprehension solution
# --------------- Runtime 27 ms, beats 91.99%. Memory 13.9MB, beats 48.11% ---------------


class Solution2:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(
            [1 for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
        )
