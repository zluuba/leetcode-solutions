# https://leetcode.com/problems/check-if-it-is-a-straight-line/

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.

# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

# --------------- Runtime 79 ms, beats 30.76%. Memory 17MB, beats 8% ---------------
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        diff_x = coordinates[1][0] - coordinates[0][0]
        diff_y = coordinates[1][1] - coordinates[0][1]

        x, y = coordinates[0]

        for curr_x, curr_y in coordinates:
            if (curr_x - x) * diff_y != (curr_y - y) * diff_x:
                return False

        return True
