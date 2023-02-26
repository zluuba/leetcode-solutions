# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.

# --------------- Runtime 63 ms, beats 55.86%. Memory 13.9MB, beats 67.34% ---------------


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        step1 = cost[0]
        step2 = cost[1]

        for i in range(2, len(cost)):
            step1, step2 = step2, min(step1, step2) + cost[i]

        return min(step1, step2)
