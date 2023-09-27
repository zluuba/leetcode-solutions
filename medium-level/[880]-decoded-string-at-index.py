# https://leetcode.com/problems/decoded-string-at-index/

# You are given an encoded string s.
# To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:
#  - If the character read is a letter, that letter is written onto the tape.
#  - If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
# Given an integer k, return the kth letter (1-indexed) in the decoded string.

# Example 1:
# Input: s = "leet2code3", k = 10
# Output: "o"
# Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10th letter in the string is "o".

# Example 2:
# Input: s = "ha22", k = 5
# Output: "h"
# Explanation: The decoded string is "hahahaha".
# The 5th letter is "h".

# Example 3:
# Input: s = "a2345678999999999999999", k = 1
# Output: "a"
# Explanation: The decoded string is "a" repeated 8301530446056247680 times.
# The 1st letter is "a".

# --------------- Runtime 40 ms, beats 37.37%. Memory 16.3MB, beats 65.15% ---------------

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_length = 0

        for char in s:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1

        for char in reversed(s):
            if char.isdigit():
                decoded_length //= int(char)
                k %= decoded_length
            else:
                if k == 0 or decoded_length == k:
                    return char

                decoded_length -= 1
