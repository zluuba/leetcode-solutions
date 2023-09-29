# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# --------------- Runtime 46 ms, beats 88.60%. Memory 16.7MB, beats 96.15% ---------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = dict(), dict()

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            s_dict[s_char] = s_dict.get(s_char, 0) + 1
            t_dict[t_char] = t_dict.get(t_char, 0) + 1

        return s_dict == t_dict


# Alternative solution - lazy
# --------------- Runtime 54 ms, beats 59.77%. Memory 18MB, beats 12.77% ---------------

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
