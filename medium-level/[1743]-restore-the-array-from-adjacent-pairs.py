# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

# There is an integer array nums that consists of n unique elements, but you have forgotten it.
# However, you do remember every pair of adjacent elements in nums.
# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates
# that the elements ui and vi are adjacent in nums.
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs,
# either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
# Return the original array nums. If there are multiple solutions, return any of them.

# Example 1:
# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.

# Example 2:
# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.

# Example 3:
# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]

# --------------- Runtime 845 ms, beats 98.59%. Memory 65.1MB, beats 77.62% ---------------
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs_dict = dict()

        for u, v in adjacentPairs:
            pairs_dict.setdefault(u, []).append(v)
            pairs_dict.setdefault(v, []).append(u)

        singles = [key for key, val in pairs_dict.items() if len(val) == 1]
        first_elem = prev = singles[0]
        result = [first_elem]

        while pairs_dict[prev]:
            curr = pairs_dict[prev].pop()
            result.append(curr)

            pairs_dict[curr].remove(prev)
            prev = curr

        return result
