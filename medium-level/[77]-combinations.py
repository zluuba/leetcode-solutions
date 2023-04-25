# https://leetcode.com/problems/combinations/

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

# --------------- Runtime 61 ms, beats 84.66%. Memory 15.2MB, beats 41.36% ---------------
from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def walker(curr):
            if len(stack) == k:
                result.append(stack[:])
                return
            if curr > n:
                return

            stack.append(curr)
            walker(curr + 1)

            stack.pop()
            walker(curr + 1)

        stack, result = [], []
        walker(1)
        return result


# Alternative solution - itertools lib
# --------------- Runtime 68 ms, beats 99.77%. Memory 14.9MB, beats 98.79% ---------------

class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(range(1, n + 1), k)
