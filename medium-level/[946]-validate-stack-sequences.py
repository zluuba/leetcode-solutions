# https://leetcode.com/problems/validate-stack-sequences/

# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result
# of a sequence of push and pop operations on an initially empty stack, or false otherwise.

# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# Example 2:
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.

# --------------- Runtime 77 ms, beats 36.36%. Memory 14MB, beats 85.31% ---------------
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        while pushed and popped:
            if stack and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
            elif pushed:
                num = pushed.pop(0)
                stack.append(num)

        return popped == stack[::-1]
