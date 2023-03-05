# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.


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
