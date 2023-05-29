# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

# Given a wooden stick of length n units. The stick is labelled from 0 to n.

# Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.
# You should perform the cuts in order, you can change the order of the cuts as you wish.

# The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts.
# When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the
# stick before the cut). Please refer to the first example for a better explanation.

# Return the minimum total cost of the cuts.

# Example 1:
# Input: n = 7, cuts = [1,3,4,5]
# Output: 16
# Explanation:
# The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6
# (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod
# of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
# Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16
# (as shown in the example photo 7 + 4 + 3 + 2 = 16).

# Example 2:
# Input: n = 9, cuts = [5,6,1,4,2]
# Output: 22
# Explanation: If you try the given cuts ordering the cost will be 25.
# There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22
# which is the minimum possible.

# --------------- Runtime 2228 ms, beats 14.93%. Memory 20.4MB, beats 10.37% ---------------
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cache = {}

        def dfs(left, right):
            if right - left == 1:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]

            result = float('inf')
            for cut in cuts:
                if left < cut < right:
                    result = min(
                        result,
                        (right - left) + dfs(left, cut) + dfs(cut, right)
                    )
            result = 0 if result == float('inf') else result
            cache[(left, right)] = result
            return result

        return dfs(0, n)
