# https://leetcode.com/problems/word-pattern/

# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# --------------- Runtime 29 ms, beats 95.3%. Memory 16.2MB, beats 89.37% ---------------

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        matches = []

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if (char not in pattern[:i]) and (word not in words[:i]):
                matches.append((char, word))
            elif (char, word) in matches:
                continue
            else:
                return False

        return True
