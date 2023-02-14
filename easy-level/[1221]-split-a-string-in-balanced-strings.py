# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s, split it into some number of substrings such that:
#
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

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
