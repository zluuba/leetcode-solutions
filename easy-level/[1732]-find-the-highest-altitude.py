# https://leetcode.com/problems/find-the-highest-altitude/

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude
# between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# Example 1:
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Example 2:
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

# --------------- Runtime 56 ms, beats 17.96%. Memory 16.3MB, beats 51.91% ---------------
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = highest = 0

        for i in range(len(gain)):
            curr += gain[i]
            highest = max(highest, curr)

        return highest


# Alternative solution - using array
# --------------- Runtime 43 ms, beats 72.74%. Memory 16.4MB, beats 15.35% ---------------

class Solution2:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        altitudes = [curr]

        for i in range(len(gain)):
            curr += gain[i]
            altitudes.append(curr)

        return max(altitudes)
