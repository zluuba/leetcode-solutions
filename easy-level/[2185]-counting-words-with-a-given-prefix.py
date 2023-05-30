# https://leetcode.com/problems/counting-words-with-a-given-prefix/

# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

# Example 1:
# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

# Example 2:
# Input: words = ["leetcode","win","loops","success"], pref = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.

# --------------- Runtime 59 ms, beats 23.84%. Memory 16.5MB, beats 20.55% ---------------
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter = 0

        for word in words:
            if word.startswith(pref):
                counter += 1

        return counter


# Alternative solution - list comprehension
# --------------- Runtime 63 ms, beats 12.33%. Memory 16.4MB, beats 49.33% ---------------

class Solution2:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = [1 for word in words if word.startswith(pref)]
        return sum(result)


# Alternative solution - without .startswith(), using filter
# --------------- Runtime 55 ms, beats 37.82%. Memory 16.3MB, beats 49.33% ---------------

class Solution3:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len(list(filter(lambda word: word[:len(pref)] == pref, words)))
