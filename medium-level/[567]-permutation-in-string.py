# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.

# --------------- Runtime 1698 ms, beats 19.45%. Memory 13.9MB, beats 60.41% ---------------
from typing import Dict
from collections import Counter


class Solution:
    def count(self, string: str) -> Dict:
                dic = dict()
                counter = Counter(string)
                for char in set(string):
                    dic[char] = counter[char]
                return dic

    def checkInclusion(self, s1: str, s2: str) -> bool:
            length = 0
            length_s1 = len(s1)
            count_s1 = self.count(s1)

            while length_s1 < len(s2) + 1:
                if count_s1 == self.count(s2[length:length_s1]):
                    return True
                length += 1
                length_s1 += 1

            return False
