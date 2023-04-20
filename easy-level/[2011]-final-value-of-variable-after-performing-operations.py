# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

# There is a programming language with only four operations and one variable X:
# - ++X and X++ increments the value of the variable X by 1.
# - --X and X-- decrements the value of the variable X by 1.

# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations,
# return the final value of X after performing all the operations.

# Example 1:
# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.

# Example 2:
# Input: operations = ["++X","++X","X++"]
# Output: 3
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# ++X: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# X++: X is incremented by 1, X = 2 + 1 = 3.

# --------------- Runtime 49 ms, beats 88.60%. Memory 13.7MB, beats 94.60% ---------------
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = [1 if op in ('++X', 'X++') else -1 for op in operations]
        return sum(result)
