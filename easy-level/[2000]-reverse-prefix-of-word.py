# https://leetcode.com/problems/reverse-prefix-of-word/

# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at
# the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and
# ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

# Example 1:
# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

# Example 2:
# Input: word = "xyxzxe", ch = "z"
# Output: "zxyxxe"
# Explanation: The first and only occurrence of "z" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

# Example 3:
# Input: word = "abcd", ch = "z"
# Output: "abcd"
# Explanation: "z" does not exist in word.
# You should not do any reverse operation, the resulting string is "abcd".

# --------------- Runtime 35 ms, beats 93.76%. Memory 16.3MB, beats 25.90% ---------------

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        prefix = word.index(ch) + 1
        new_word = word[:prefix][::-1] + word[prefix:]

        return new_word


# Alternative solution - short
# --------------- Runtime 51 ms, beats 25.83%. Memory 16.2MB, beats 65.36% ---------------

class Solution2:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = word.find(ch) + 1
        return word[:prefix][::-1] + word[prefix:]
