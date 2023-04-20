# https://leetcode.com/problems/split-a-string-in-balanced-strings/

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:
# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

# Example 3:
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".

# --------------- Runtime 28 ms, beats 87.61%. Memory 13.8MB, beats 49.82% ---------------


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        temp = 0
        for char in s:
            if char == 'R':
                temp += 1
            else:
                temp -= 1

            if temp == 0:
                result += 1

        return result


# Alternative solution
# --------------- Runtime 38 ms, beats 36.26%. Memory 13.8MB, beats 49.82% ---------------


class Solution2:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        temp = ''
        for char in s:
            temp += char

            if temp.count('L') == temp.count('R'):
                result += 1
                temp = ''

        return result
