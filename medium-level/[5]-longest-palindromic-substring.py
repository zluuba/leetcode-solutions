# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# --------------- Runtime 4036 ms, beats 19.29%. Memory 16.2MB, beats 97.9% ---------------
# Yes, it does have a long runtime, but I enjoyed the process, so it doesn't count as long as it's fun

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        result = ''

        for left in range(length):
            result_length = len(result)

            for right in range(length, left, -1):
                curr_length = right - left + 1
                subs = s[left:right]

                if result_length >= curr_length:
                    break

                if subs == subs[::-1]:
                    result = s[left:right]
                    break

            if result_length >= length - left:
                break

        return result
