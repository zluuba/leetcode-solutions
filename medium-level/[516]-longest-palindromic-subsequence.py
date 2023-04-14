# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or
# no elements without changing the order of the remaining elements.

# Example 1:
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".

# Example 2:
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".

# --------------- Runtime 1868 ms, beats 44.56%. Memory 39.9MB, beats 40.9% ---------------


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)

        if len(set(s)) == 1:
            return length

        mtx = [[0] * (length + 1) for _ in range(length + 1)]
        reverse_s = s[::-1]

        for i in range(length - 1, -1, -1):
            for j in range(length - 1, -1, -1):
                if s[i] == reverse_s[j]:
                    mtx[i][j] = 1 + mtx[i + 1][j + 1]
                else:
                    mtx[i][j] = max(mtx[i + 1][j], mtx[i][j + 1])

        return mtx[0][0]
