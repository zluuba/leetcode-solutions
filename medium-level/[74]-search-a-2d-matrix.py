# https://leetcode.com/problems/search-a-2d-matrix/

# You are given an m x n integer matrix with the following two properties:
#  - Each row is sorted in non-decreasing order.
#  - The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# --------------- Runtime 49 ms, beats 90.75%. Memory 16.7MB, beats 99.39% ---------------
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_row(l, r):
            while l <= r:
                mid_row = l + (r - l) // 2

                if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                    return mid_row
                elif matrix[mid_row][0] < target:
                    l = mid_row + 1
                else:
                    r = mid_row - 1
            return -1

        def search(row, l, r):
            while l <= r:
                mid = l + (r - l) // 2

                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        row = get_row(0, len(matrix) - 1)
        return search(row, 0, len(matrix[0]) - 1)
