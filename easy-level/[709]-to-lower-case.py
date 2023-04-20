# https://leetcode.com/problems/to-lower-case/

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

# Example 1:
# Input: s = "Hello"
# Output: "hello"

# Example 2:
# Input: s = "here"
# Output: "here"

# Example 3:
# Input: s = "LOVELY"
# Output: "lovely"

# --------------- Runtime 61 ms, beats 84.66%. Memory 15.2MB, beats 41.36% ---------------


class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()

        return ''.join(
            [chr(ord(char) + 32) if (65 <= ord(char) <= 90) else char for char in s]
        )
