# You are given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#
# Return the shuffled string.

# --------------- Runtime 49 ms, beats 95.59%. Memory 13.8MB, beats 52.90% ---------------


class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [''] * len(s)
        for ind, n in enumerate(indices):
            result[n] = s[ind]

        return ''.join(result)
