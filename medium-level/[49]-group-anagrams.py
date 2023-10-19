# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# --------------- Runtime 61 ms, beats 84.66%. Memory 15.2MB, beats 41.36% ---------------
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for s in strs:
            sorted_s = tuple(sorted(list(s)))
            anagrams[sorted_s] = anagrams.get(sorted_s, []) + [s]

        group_anagrams = [val for val in anagrams.values()]
        return group_anagrams
