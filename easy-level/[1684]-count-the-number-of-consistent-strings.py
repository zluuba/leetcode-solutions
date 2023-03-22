# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.
#
# Example:
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# --------------- Runtime 286 ms, beats 23.71%. Memory 15.9MB, beats 98.48% ---------------
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0

        for word in words:
            if set(word).issubset(set(allowed)):
                result += 1

        return result


# --------------- Runtime 270 ms, beats 33.84%. Memory 16MB, beats 40.45% ---------------

# Alternative solution. Shortest
class Solution2:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = [1 for word in words if set(word).issubset(set(allowed))]
        return sum(result)