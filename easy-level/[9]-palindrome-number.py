# Given an integer x, return true if x is a palindrome, and false otherwise.

# --------------- Runtime 59 ms, beats 81.43%. Memory 13.8MB, beats 95.10% ---------------


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
