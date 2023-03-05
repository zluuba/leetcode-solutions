# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

# --------------- Runtime 44 ms, beats 34.29%. Memory 13.9MB, beats 42.46% ---------------
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for ind, char in enumerate(strs[0]):
            for char2 in strs[1:]:
                if len(char2) - 1 < ind or char != char2[ind]:
                    return res
            res += char
        return res
