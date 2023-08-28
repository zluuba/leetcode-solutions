# https://leetcode.com/problems/valid-palindrome/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# --------------- Runtime 45 ms, beats 89.62%. Memory 17.9MB, beats 27.26% ---------------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(filter(lambda char: char.isalnum(), s)).lower()
        return string == string[::-1]
