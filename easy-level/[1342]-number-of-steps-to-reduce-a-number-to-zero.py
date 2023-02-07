# Given an integer num, return the number of steps to reduce it to zero.
#
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# --------------- Runtime 34 ms, beats 60.86%. Memory 13.8MB, beats 93.90% ---------------


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            steps += 1
        return steps
