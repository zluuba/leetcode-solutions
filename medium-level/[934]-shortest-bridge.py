# https://leetcode.com/problems/shortest-bridge/

# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
# An island is a 4-directionally connected group of 1's not connected to any other 1's.
# There are exactly two islands in grid.
# You may change 0's to 1's to connect the two islands to form one island.
# Return the smallest number of 0's you must flip to connect the two islands.

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 1

# Example 2:
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2

# Example 3:
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1

# --------------- Runtime 422 ms, beats 44.76%. Memory 21.9MB, beats 9.60% ---------------
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        length = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visit = set()

        def invalid(r, c):
            return r < 0 or r >= length or c < 0 or c >= length

        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            result, q = 0, list(visit)
            while q:
                length_q = len(q)
                for i in range(length_q):
                    r, c = q.pop(0)
                    for dr, dc in directions:
                        curr_r, curr_c = r + dr, c + dc
                        if invalid(curr_r, curr_c) or (curr_r, curr_c) in visit:
                            continue
                        if grid[curr_r][curr_c]:
                            return result

                        q.append((curr_r, curr_c))
                        visit.add((curr_r, curr_c))
                result += 1

        for r in range(length):
            for c in range(length):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()
