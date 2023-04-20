# https://leetcode.com/problems/sort-the-people/

# You are given an array of strings names, and an array heights that consists of distinct positive integers.
# Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

# Example 1:
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.

# Example 2:
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

# --------------- Runtime 112 ms, beats 89.19%. Memory 14.4MB, beats 37.12% ---------------
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        sorted_people = sorted(people, key=lambda x: -x[1])

        return list(map(lambda x: x[0], sorted_people))
