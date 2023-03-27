# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings,
# and + represents string concatenation.
#
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it
# into s = A + B, with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk,
# where Pi are primitive valid parentheses strings.
#
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

# Example:
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

# --------------- Runtime 39 ms, beats 65.71%. Memory 13.9MB, beats 87.25% ---------------


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''

        if s.count('((') < 1:
            return result

        stack = []
        for i in s:
            stack.append(i)
            if stack and stack.count('(') == stack.count(')'):
                part = ''.join(stack)
                result += part[1:-1]
                stack = []

        return result
