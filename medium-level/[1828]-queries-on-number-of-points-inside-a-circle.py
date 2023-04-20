# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

# You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane.
# Multiple points can have the same coordinates.
# You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj)
# with a radius of rj.
# For each query queries[j], compute the number of points inside the jth circle.
# Points on the border of the circle are considered inside.
# Return an array answer, where answer[j] is the answer to the jth query.

# Example 1:
# Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
# Output: [3,2,2]
# Explanation: The points and circles are shown above.
# queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.

# Example 2:
# Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
# Output: [2,3,2,4]
# Explanation: The points and circles are shown above.
# queries[0] is green, queries[1] is red, queries[2] is blue, and queries[3] is purple.

# --------------- Runtime 2285 ms, beats 50.50%. Memory 14.2MB, beats 43.88% ---------------
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []

        for circle in queries:
            cx, cy, radius = circle
            points_inside = 0

            for point in points:
                px, py = point

                distance = (px - cx) ** 2 + (py - cy) ** 2
                if distance <= radius ** 2:
                    points_inside += 1

            result.append(points_inside)

        return result
