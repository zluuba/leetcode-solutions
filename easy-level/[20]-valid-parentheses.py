# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# --------------- Runtime 35 ms, beats 59.98%. Memory 13.9MB, beats 19.65% ---------------


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ('(', '[', '{')
        close_brackets = (')', ']', '}')

        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)
            elif stack and stack[-1] == brackets[close_brackets.index(char)]:
                stack.pop()
            else:
                return False
        return True if not stack else False
