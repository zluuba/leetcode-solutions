# https://leetcode.com/problems/maximum-length-of-pair-chain/

# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.

# Example 1:
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].

# Example 2:
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

# --------------- Runtime 196 ms, beats 75.54%. Memory 17MB, beats 33.19% ---------------
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])
        prev = pairs[0][1]
        result = 1

        for curr in pairs[1:]:
            if prev < curr[0]:
                result += 1
                prev = curr[1]

        return result
