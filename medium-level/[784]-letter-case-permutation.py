# https://leetcode.com/problems/letter-case-permutation/description/?envType=study-plan&id=algorithm-i

# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.

# Example 1:
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

# Example 2:
# Input: s = "3z4"
# Output: ["3z4","3Z4"]

# --------------- Runtime 58 ms, beats 62.28%. Memory 15.5MB, beats 18.92% ---------------
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        length = len(s)
        result = []

        def swapover(sub, i):
            if len(sub) == length:
                result.append(sub)
                return

            if s[i].isalpha():
                swapover(sub + s[i].swapcase(), i + 1)
            swapover(sub + s[i], i + 1)

        swapover('', 0)
        return result


# Alternative solution (half-alternative) - more readable
# --------------- Runtime 50 ms, beats 90.80%. Memory 15.4MB, beats 18.92% ---------------

class Solution2:
    def letterCasePermutation(self, s: str) -> List[str]:
        length = len(s)
        result = []

        def swapover(sub, i):
            if len(sub) == length:
                result.append(sub)
                return

            if s[i].isalpha():
                swapover(sub + s[i].upper(), i + 1)
                swapover(sub + s[i].lower(), i + 1)
            else:
                swapover(sub + s[i], i + 1)

        swapover('', 0)
        return result
