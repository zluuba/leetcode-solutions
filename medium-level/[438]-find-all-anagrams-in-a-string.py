# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Given two strings s and p, return an array of all the start indices of p's anagrams in s.
# You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# --------------- Runtime 3976 ms, beats 13.65%. Memory 15.2MB, beats 27% ---------------
from typing import List


class Solution:
    def get_dict(self, string):
        d = dict()
        for char in set(string):
            count = string.count(char)
            d[char] = count
        return d

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        dict_p = self.get_dict(p)

        for ind, char in enumerate(s):
            if len(s) - ind < len(p):
                break
            chunk = s[ind:len(p) + ind]
            dict_chunk = self.get_dict(chunk)

            if dict_chunk == dict_p:
                res.append(ind)
        return res
