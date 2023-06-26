# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

# You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.
# You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi.
# For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.
# Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.
# Return the number of rectangles that can make a square with a side length of maxLen.

# Example 1:
# Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
# Output: 3
# Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
# The largest possible square is of length 5, and you can get it out of 3 rectangles.

# Example 2:
# Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
# Output: 3

# --------------- Runtime 203 ms, beats 66.54%. Memory 17MB, beats 20.23% ---------------
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = []

        for rect in rectangles:
            l, w = rect

            if l < w:
                squares.append([l, l])
            else:
                squares.append([w, w])

        max_rect = max(squares)
        return squares.count(max_rect)


# Alternative solution - short
# --------------- Runtime 220 ms, beats 7.78%. Memory 16.8MB, beats 92.2% ---------------

class Solution2:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = [[l, l] if l < w else [w, w] for l, w in rectangles]
        return squares.count(max(squares))
