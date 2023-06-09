# https://leetcode.com/problems/unique-number-of-occurrences/

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique
# or false otherwise.

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:
# Input: arr = [1,2]
# Output: false
# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

# --------------- Runtime 51 ms, beats 58.79%. Memory 16.5MB, beats 10.29% ---------------
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = []

        for char in set(arr):
            count = arr.count(char)
            if count in occurrences:
                return False

            occurrences.append(count)

        return True


# Alternative solution - using collections.Counter
# --------------- Runtime 53 ms, beats 50.67%. Memory 16.5MB, beats 40.10% ---------------
from collections import Counter


class Solution2:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(set(c.values())) == len(c.values())
