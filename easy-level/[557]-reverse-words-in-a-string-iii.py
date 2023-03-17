# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

# Example:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# --------------- Runtime 35 ms, beats 77.14%. Memory 14.6MB, beats 38.74% ---------------


class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_words = [word[::-1] for word in s.split()]
        return ' '.join(reverse_words)
