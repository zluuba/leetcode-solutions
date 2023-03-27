# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.
#
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#
# For example, inverting [0,1,1] results in [1,0,0].

# Example:
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]


# --------------- Runtime 51 ms, beats 72.53%. Memory 13.8MB, beats 52.56% ---------------
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []

        for line in image:
            flipped_line = [1 - num for num in line]
            result.append(reversed(flipped_line))

        return result
