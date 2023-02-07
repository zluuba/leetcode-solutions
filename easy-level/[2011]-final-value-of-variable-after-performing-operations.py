# There is a programming language with only four operations and one variable X:
#
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
#
# Given an array of strings operations containing a list of operations,
# return the final value of X after performing all the operations.

# --------------- Runtime 49 ms, beats 88.60%. Memory 13.7MB, beats 94.60% ---------------


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        result = [1 if op in ('++X', 'X++') else -1 for op in operations]
        return sum(result)
