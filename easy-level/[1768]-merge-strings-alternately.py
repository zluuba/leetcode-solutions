# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other, append the additional letters onto the end
# of the merged string.
# Return the merged string.

# Example:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# --------------- Runtime 32 ms, beats 63.30%. Memory 13.8MB, beats 95.97% ---------------


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        m = min(len1, len2)

        tail = word1[m:] if len1 > len2 else word2[m:]
        result = ''.join(map(lambda t: t[0] + t[1], zip(word1, word2)))

        return result + tail


# Alternative solution - loop, no funcs
# --------------- Runtime 35 ms, beats 42.24%. Memory 13.9MB, beats 9.46% ---------------

class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1, length2 = len(word1), len(word2)
        result = ''

        for i in range(min(length1, length2)):
            result += word1[i] + word2[i]

        if length1 != length2:
            result += word1[i + 1:] if length1 > length2 else word2[i + 1:]

        return result
