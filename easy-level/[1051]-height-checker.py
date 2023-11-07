# https://leetcode.com/problems/height-checker/

# A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing order by height.
# Let this ordering be represented by the integer array expected where expected[i] is the
# expected height of the ith student in line.
# You are given an integer array heights representing the current order that the students are standing in.
# Each heights[i] is the height of the ith student in line (0-indexed).
# Return the number of indices where heights[i] != expected[i].

# Example:
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

# --------------- Runtime 38 ms, beats 83.9%. Memory 16.2MB, beats 68% ---------------
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        result = [i for i in range(len(heights)) if heights[i] != sorted_heights[i]]

        return len(result)


# Alternative solution - clear for-loop
# --------------- Runtime 44 ms, beats 49.98%. Memory 16.2MB, beats 68% ---------------

class Solution2:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        result = 0

        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                result += 1

        return result
