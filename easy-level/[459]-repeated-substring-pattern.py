# https://leetcode.com/problems/repeated-substring-pattern/

# Given a string s, check if it can be constructed by taking a substring of it and
# appending multiple copies of the substring together.

# Example 1:
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

# Example 2:
# Input: s = "aba"
# Output: false

# Example 3:
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

# --------------- Runtime 109 ms, beats 36.39%. Memory 16.4MB, beats 75.82% ---------------

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)

        for i in range(1, length // 2 + 1):
            subs = s[0:i] * (length // i)

            if s == subs:
                return True

        return False
