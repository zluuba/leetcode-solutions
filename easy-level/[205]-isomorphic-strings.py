# https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

# --------------- Runtime 42 ms, beats 69.13%. Memory 14.2MB, beats 83.59% ---------------


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        compliance = {}

        if len(set(s)) != len(set(t)):
            return False

        for ind, char in enumerate(s):
            if char not in compliance:
                compliance[char] = t[ind]
            else:
                if compliance[char] != t[ind]:
                    return False
        return True
