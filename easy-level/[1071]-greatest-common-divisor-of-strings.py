# https://leetcode.com/problems/greatest-common-divisor-of-strings/

# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

# --------------- Runtime 57 ms, beats 17.43%. Memory 16.4MB, beats 29.97% ---------------

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shortest, largest = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        result = shortest

        while result:
            candidat_l = result * (len(largest) // len(result))
            candidat_s = result * (len(shortest) // len(result))

            if candidat_l == largest and candidat_s == shortest:
                break

            result = result[:-1]

        return result
