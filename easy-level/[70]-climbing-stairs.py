# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# --------------- Runtime 34 ms, beats 50.54%. Memory 13.8MB, beats 94.63% ---------------


class Solution:
    def climbStairs(self, n: int) -> int:
        point1, point2 = 1, 1
        for i in range(n - 1):
            point1, point2 = point1 + point2, point1

        return point1
