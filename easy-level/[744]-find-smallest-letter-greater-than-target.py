# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
# There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.

# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

# --------------- Runtime 137 ms, beats 40.24%. Memory 16.5MB, beats 67.25% ---------------
from typing import List
import string


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        abc = string.ascii_lowercase
        result_ind = 27

        for char in set(letters):
            if char > target:
                result_ind = min(result_ind, abc.find(char))

        return abc[result_ind] if result_ind < 27 else letters[0]


# Alternative solution
# --------------- Runtime 137 ms, beats 40.24%. Memory 16.8MB, beats 21.82% ---------------

class Solution2:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target != 'z':
            for char in letters:
                if char > target:
                    return char
        return letters[0]
