# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".

# Example 1:
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")

# Example 2:
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".

# Example 3:
# Input: s = "bbcbaba"
# Output: 4

# --------------- Runtime 257 ms, beats 60.97%. Memory 17.3MB, beats 24.34% ---------------
from collections import Counter, defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        length = len(s)
        result = 0

        for char, count in Counter(s).items():
            left, right = 0, length - 1

            while s[left] != char:
                left += 1
            while s[right] != char:
                right -= 1

            middle_chars = set(s[left + 1: right])
            result += len(middle_chars)

        return result


# Alternative solution - indices and min/max
# --------------- Runtime 243 ms, beats 62.39%. Memory 25.8MB, beats 5.26% ---------------

class Solution2:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_by_indices = defaultdict(set)
        result = 0

        for index, char in enumerate(s):
            char_by_indices[char].add(index)

        for char, indices in char_by_indices.items():
            left, right = min(indices), max(indices)

            middle_chars_count = len(set(s[left + 1: right]))
            result += middle_chars_count

        return result
