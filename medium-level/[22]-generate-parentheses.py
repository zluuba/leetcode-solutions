# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

# --------------- Runtime 93 ms, beats 5.12%. Memory 16.6MB, beats 88.95% ---------------
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(comb, stack):
            for bracket in comb:
                if bracket == '(':
                    stack.append(bracket)
                elif stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return stack == []

        def build_combinations(comb):
            if len(comb) == length:
                if is_valid(comb, []):
                    combinations.append(''.join(comb))
                return

            build_combinations(comb + ['('])
            build_combinations(comb + [')'])

        length = n * 2
        combinations = []
        build_combinations([])

        return combinations


# Alternative solution - shorter, smarter, but without yummy is_valid function
# --------------- Runtime 39 ms, beats 92.7%. Memory 16.7MB, beats 27.52% ---------------

class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        def build_combinations(comb, opened, closed):
            if len(comb) == length:
                combinations.append(''.join(comb))
                return

            if opened < n:
                build_combinations(comb + ['('], opened + 1, closed)

            if closed < opened:
                build_combinations(comb + [')'], opened, closed + 1)

        length = n * 2
        combinations = []
        build_combinations([], 0, 0)

        return combinations
