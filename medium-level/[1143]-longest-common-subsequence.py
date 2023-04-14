# Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

# --------------- Runtime 884 ms, beats 61.87%. Memory 40MB, beats 39.1% ---------------


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1, length2 = len(text1), len(text2)
        mtx = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for i in range(length1 - 1, -1, -1):
            for j in range(length2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    mtx[i][j] = 1 + mtx[i + 1][j + 1]
                else:
                    mtx[i][j] = max(mtx[i + 1][j], mtx[i][j + 1])

        return mtx[0][0]
