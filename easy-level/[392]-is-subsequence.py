# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# --------------- Runtime 32 ms, beats 77.52%. Memory 13.8MB, beats 98.65% ---------------


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s or s == t:
            return True

        equal = 0
        for char in t:
            if s[equal] == char:
                equal += 1
            if equal == len(s):
                return True
        return False
