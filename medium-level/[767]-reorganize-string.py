# https://leetcode.com/problems/reorganize-string/

# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.

# Example 1:
# Input: s = "aab"
# Output: "aba"

# Example 2:
# Input: s = "aaab"
# Output: ""

# --------------- Runtime 40 ms, beats 81.56%. Memory 16.3MB, beats 46.15% ---------------
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        length = len(s)

        c = Counter(s)
        max_char, max_count = max(c.items(), key=lambda x: x[1])

        if max_count > (length + 1) // 2:
            return ''

        new_s = [max_char for _ in range(max_count)]
        del c[max_char]

        i = 0
        for char, count in c.items():
            for _ in range(count):
                new_s[i] += char
                i += 1

                if i >= len(new_s):
                    i = 0

        return ''.join(new_s)
