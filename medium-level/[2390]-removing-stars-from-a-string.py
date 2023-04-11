# You are given a string s, which contains stars *.
# In one operation, you can:
# - Choose a star in s.
# - Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:
# - The input will be generated such that the operation is always possible.
# - It can be shown that the resulting string will always be unique.

# Example:
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".

# --------------- Runtime 61 ms, beats 99.65%. Memory 15.6MB, beats 77.42% ---------------


class Solution:
    def removeStars(self, s: str) -> str:
        if s.count('*') >= len(s) / 2:
            return ''

        result = []
        for char in s:
            if char == '*':
                result.pop()
            else:
                result.append(char)
        return ''.join(result)


# --------------- Runtime 2097 ms, beats 6.7%. Memory 15.4MB, beats 93.9% ---------------
# Alternative solution without creating additional arrays (string change)


class Solution2:
    def removeStars(self, s: str) -> str:
        if s.count('*') >= len(s) / 2:
            return ''

        while '*' in s:
            p1 = s.index('*')
            p2 = p1
            while s[p2] == '*':
                p2 += 1
                if p2 >= len(s) - 1:
                    break

            diff = p2 - p1
            if not diff:
                p1 -= 1
                p2 += 1

            p1 -= diff
            s = s[:p1] + s[p2:]

        return s
