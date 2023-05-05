# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

# --------------- Runtime 179 ms, beats 71.35%. Memory 18.4MB, beats 5.1% ---------------

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        s = [1 if char in vowels else 0 for char in s]

        p1, p2 = 0, k
        result = sum(s[p1:p2])
        subs = result

        while p2 < len(s):
            subs = (subs - s[p1] + s[p2])
            if subs > result:
                result = subs
            if result == k:
                return result

            p1 += 1
            p2 += 1

        return result
