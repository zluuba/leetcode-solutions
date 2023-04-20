# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
# or false otherwise.

# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

# Example 2:
# Input: sentence = "leetcode"
# Output: false

# --------------- Runtime 25 ms, beats 95.24%. Memory 13.7MB, beats 92.89% ---------------


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_volume = 26
        return len(set(sentence)) == alphabet_volume


# Alternative solution.
# --------------- Runtime 35 ms, beats 52.76%. Memory 13.8MB, beats 92.89% ---------------
import string


class Solution2:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set(string.ascii_lowercase)
        uniq_letters = set(sentence)
        return alphabet == uniq_letters
