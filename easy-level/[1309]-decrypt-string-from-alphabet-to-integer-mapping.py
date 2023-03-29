# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
#
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
#
# The test cases are generated so that a unique mapping will always exist.

# Example:
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

# --------------- Runtime 32 ms, beats 67.91%. Memory 13.9MB, beats 53.26% ---------------


class Solution:
    def freqAlphabets(self, s: str) -> str:
        result, i = '', 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num_char = int(s[i] + s[i + 1])
                i += 3
            else:
                num_char = int(s[i])
                i += 1
            char = chr(num_char + 96)
            result += char

        return result
