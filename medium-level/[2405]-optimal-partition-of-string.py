# Given a string s, partition the string into one or more substrings such that the characters in each substring
# are unique. That is, no letter appears in a single substring more than once.
# Return the minimum number of substrings in such a partition.
# Note that each character should belong to exactly one substring in a partition.

# Example:
# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.

# --------------- Runtime 88 ms, beats 95.25%. Memory 14.7MB, beats 47.10% ---------------


class Solution:
    def partitionString(self, s: str) -> int:
        counter = 1
        substring = ''

        for char in s:
            if char in substring:
                counter += 1
                substring = ''
            substring += char

        return counter
