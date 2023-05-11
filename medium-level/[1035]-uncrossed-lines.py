# https://leetcode.com/problems/uncrossed-lines/

# You are given two integer arrays nums1 and nums2.
# We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
# - nums1[i] == nums2[j], and
# - the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints
# (i.e., each number can only belong to one connecting line).

# Return the maximum number of connecting lines we can draw in this way.

# Example 1:
# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line
# from nums1[2]=2 to nums2[1]=2.

# Example 2:
# Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
# Output: 3

# Example 3:
# Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
# Output: 2

# --------------- Runtime 156 ms, beats 95.1%. Memory 16.2MB, beats 40.94% ---------------
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        length1, length2 = len(nums1), len(nums2)
        dp = [0] * (length2 + 1)

        for i in range(length1):
            new_dp = [0] * (length2 + 1)

            for j in range(length2):
                if nums1[i] == nums2[j]:
                    new_dp[j + 1] = 1 + dp[j]
                else:
                    new_dp[j + 1] = max(
                        new_dp[j], dp[j + 1]
                    )
            dp = new_dp

        return new_dp[length2]


# Alternative solution - dynamic programming, O(n * m)
# Like prev solution, but not optimized (stores all rows instead of two rows)
# --------------- Runtime 192 ms, beats 67.19%. Memory 16.7MB, beats 29.13% ---------------

class Solution2:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        length1, length2 = len(nums1), len(nums2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for i in range(length1):
            for j in range(length2):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(
                        dp[i + 1][j], dp[i][j + 1]
                    )

        return dp[length1][length2]


# Alternative solution - recursion, O(n * m)
# --------------- Runtime 505 ms, beats 5.25%. Memory 61.4MB, beats 5.25% ---------------

class Solution3:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            if nums1[i] == nums2[j]:
                dp[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

            return dp[(i, j)]

        dp = {}
        return dfs(0, 0)
