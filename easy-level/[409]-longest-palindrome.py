# https://leetcode.com/problems/longest-palindrome/

# Given a string s which consists of lowercase or uppercase letters, return the length
# of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

# --------------- Runtime 27 ms, beats 95.41%. Memory 13.8MB, beats 96.74% ---------------


class Solution:
    def longestPalindrome(self, s: str) -> int:
        palindrome, odds = 0, 0

        for char in set(s):
            value = s.count(char)
            if value % 2 != 0:
                odds += 1
            palindrome += value

        return (palindrome - odds) + (1 if odds else 0)
