# https://leetcode.com/problems/decode-string/

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
# exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces,
# square brackets are well-formed, etc. Furthermore, you may assume that the original data
# does not contain any digits and that digits are only for those repeat numbers, k.
# For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 10^5.

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# --------------- Runtime 34 ms, beats 51.10%. Memory 13.9MB, beats 60.86% ---------------


class Solution:
    def decodeString(self, s: str) -> str:
        if s.isdigit():
            return ''

        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * substr)

        return ''.join(stack)
