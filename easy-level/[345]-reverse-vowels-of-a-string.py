# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# --------------- Runtime 66 ms, beats 66.42%. Memory 17.3MB, beats 54.39% ---------------

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            if s[p1] in vowels and s[p2] in vowels:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
            elif s[p1] in vowels:
                p2 -= 1
            elif s[p2] in vowels:
                p1 += 1
            else:
                p1 += 1
                p2 -= 1

        return ''.join(s)
