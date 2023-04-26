# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# --------------- Runtime 32 ms, beats 57.30%. Memory 13.8MB, beats 94.22% ---------------


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        return haystack.index(needle)


# Alternative solution - sliding window
# --------------- Runtime 46 ms, beats 8.1%. Memory 16.2MB, beats 9.5% ---------------

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        p1, p2 = 0, len(needle)

        while p2 <= len(haystack):
            if haystack[p1:p2] == needle:
                return p1
            p1 += 1
            p2 += 1

        return -1
