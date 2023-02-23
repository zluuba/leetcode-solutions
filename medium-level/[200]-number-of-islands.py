# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number
# of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# --------------- Runtime 444 ms, beats 17.34%. Memory 21.9MB, beats 25.45% ---------------


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit, islands = set(), 0

        def search(row, col):
            q = []
            visit.add((row, col))
            q.append((row, col))

            while q:
                r, c = q.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows)) and col in range(cols) and \
                            grid[row][col] == '1' and (row, col) not in visit:
                        q.append((row, col))
                        visit.add((row, col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visit:
                    search(row, col)
                    islands += 1

        return islands
