# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string.
# For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Example 1:
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.

# Example 2:
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

# Example 3:
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

# --------------- Runtime 172 ms, beats 50.35%. Memory 16.9MB, beats 99.72% ---------------

class Solution:
    def minDeletions(self, s: str) -> int:
        letters = dict()

        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1

        frequencies = []
        result = 0

        for frequency in letters.values():
            while frequency and frequency in frequencies:
                frequency -= 1
                result += 1

            frequencies.append(frequency)

        return result
