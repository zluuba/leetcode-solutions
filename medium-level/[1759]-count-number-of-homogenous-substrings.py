# https://leetcode.com/problems/count-number-of-homogenous-substrings/

# Given a string s, return the number of homogenous substrings of s.
# Since the answer may be too large, return it modulo 109 + 7.
# A string is homogenous if all the characters of the string are the same.
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "abbcccaa"
# Output: 13
# Explanation: The homogenous substrings are listed as below:
# "a"   appears 3 times.
# "aa"  appears 1 time.
# "b"   appears 2 times.
# "bb"  appears 1 time.
# "c"   appears 3 times.
# "cc"  appears 2 times.
# "ccc" appears 1 time.
# 3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

# Example 2:
# Input: s = "xy"
# Output: 2
# Explanation: The homogenous substrings are "x" and "y".

# Example 3:
# Input: s = "zzzzz"
# Output: 15

# --------------- Runtime 93 ms, beats 90.65%. Memory 16.9MB, beats 99.64% ---------------

class Solution:
    def countHomogenous(self, s: str) -> int:
        result = 1
        subs_count = 1
        prev_char = s[0]

        for char in s[1:]:
            if char == prev_char:
                subs_count += 1
            else:
                subs_count = 1
                prev_char = char

            result += subs_count

        return result % (10 ** 9 + 7)
