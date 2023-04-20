# https://leetcode.com/problems/length-of-last-word/

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


# --------------- Runtime 23 ms, beats 97.28%. Memory 13.9MB, beats 73.47% ---------------


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last_word = words[-1]
        return len(last_word)


# Alternative solution. One line
# --------------- Runtime 25 ms, beats 93.61%. Memory 14MB, beats 31.77% ---------------


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
