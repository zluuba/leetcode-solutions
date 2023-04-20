# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

# Given an array of strings patterns and a string word, return the number of strings in patterns that exist
# as a substring in word.

# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: patterns = ["a","abc","bc","d"], word = "abc"
# Output: 3
# Explanation:
# - "a" appears as a substring in "abc".
# - "abc" appears as a substring in "abc".
# - "bc" appears as a substring in "abc".
# - "d" does not appear as a substring in "abc".
# 3 of the strings in patterns appear as a substring in word.

# Example 2:
# Input: patterns = ["a","a","a"], word = "ab"
# Output: 3
# Explanation: Each of the patterns appears as a substring in word "ab".

# --------------- Runtime 36 ms, beats 69.88%. Memory 13.9MB, beats 63.68% ---------------
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([pattern for pattern in patterns if pattern in word])
