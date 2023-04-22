# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

# Given a string s. In one step you can insert any character at any index of the string.
# Return the minimum number of steps to make s palindrome.
# A Palindrome String is one that reads the same backward as well as forward.

# Example 1:
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.

# Example 2:
# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".

# Example 3:
# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".

# --------------- Runtime 1333 ms, beats 22.52%. Memory 16MB, beats 67.55% ---------------


class Solution:
    def minInsertions(self, s: str) -> int:
        reverse = s[::-1]
        length = len(s)

        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i - 1] == reverse[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j-1])

        return length - dp[length][length]
