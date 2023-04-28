# https://leetcode.com/problems/similar-string-groups/

# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.
# Also two strings X and Y are similar if they are equal.

# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar,
# but "star" is not similar to "tars", "rats", or "arts".

# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
# Notice that "tars" and "arts" are in the same group even though they are not similar.
# Formally, each group is such that a word is in the group if and only if it is similar to at least one other word
# in the group.

# We are given a list strs of strings where every string in strs is an anagram of every other string in strs.
# How many groups are there?

# Example 1:
# Input: strs = ["tars","rats","arts","star"]
# Output: 2

# Example 2:
# Input: strs = ["omv","ovm"]
# Output: 1

# --------------- Runtime 1819 ms, beats 42.95%. Memory 17MB, beats 10.16% ---------------
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        length = len(strs)
        visited = [0] * length

        def walker(ind):
            for i in range(length):
                if not visited[i]:
                    diff = 0
                    for x, y in zip(strs[ind], strs[i]):
                        if x != y:
                            diff += 1
                    if diff <= 2:
                        visited[i] = 1
                        walker(i)

        groups = 0
        for i in range(length):
            if not visited[i]:
                groups += 1
                visited[i] = 1
                walker(i)

        return groups
