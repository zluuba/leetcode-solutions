# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

# You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n,
# where obstacles[i] describes the height of the ith obstacle.
# For every index i between 0 and n - 1 (inclusive),
# find the length of the longest obstacle course in obstacles such that:
# - You choose any number of obstacles between 0 and i inclusive.
# - You must include the ith obstacle in the course.
# - You must put the chosen obstacles in the same order as they appear in obstacles.
# - Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.
# Return an array ans of length n, where ans[i] is the length of the longest obstacle course
# for index i as described above.

# Example 1:
# Input: obstacles = [1,2,3,2]
# Output: [1,2,3,3]
# Explanation: The longest valid obstacle course at each position is:
# - i = 0: [1], [1] has length 1.
# - i = 1: [1,2], [1,2] has length 2.
# - i = 2: [1,2,3], [1,2,3] has length 3.
# - i = 3: [1,2,3,2], [1,2,2] has length 3.

# Example 2:
# Input: obstacles = [2,2,1]
# Output: [1,2,1]
# Explanation: The longest valid obstacle course at each position is:
# - i = 0: [2], [2] has length 1.
# - i = 1: [2,2], [2,2] has length 2.
# - i = 2: [2,2,1], [1] has length 1.

# Example 3:
# Input: obstacles = [3,1,5,6,4,2]
# Output: [1,1,2,3,2,2]
# Explanation: The longest valid obstacle course at each position is:
# - i = 0: [3], [3] has length 1.
# - i = 1: [3,1], [1] has length 1.
# - i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
# - i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
# - i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
# - i = 5: [3,1,5,6,4,2], [1,2] has length 2.

# --------------- Runtime 1557 ms, beats 65.15%. Memory 34.6MB, beats 10.61% ---------------
from typing import List
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        result = []
        dp = [10 ** 7 + 7] * (len(obstacles) + 1)

        for num in obstacles:
            index = bisect.bisect(dp, num)  # bisect - binary search

            result.append(index + 1)
            dp[index] = num

        return result


# --------------- Runtime 1557 ms, beats 65.15%. Memory 34.6MB, beats 10.61% ---------------

class Solution2:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        length = len(obstacles)
        result = [0] * length
        dp = [0] * length
        dp_length = 0

        for i in range(length):
            left, right = 0, dp_length
            while left < right:
                middle = (left + right) >> 1
                if dp[middle] <= obstacles[i]:
                    left = middle + 1
                else:
                    right = middle

            if left >= dp_length or dp[left] > obstacles[i]:
                dp[left] = obstacles[i]
            if left == dp_length:
                dp_length += 1

            result[i] = left + 1

        return result
