# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from
# the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
# of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
#
# Return the modified image after performing the flood fill.

# --------------- Runtime 80 ms, beats 60.52%. Memory 14.2MB, beats 33.99% ---------------


class Solution:
    def fill(self, image, sr, sc, color, curr_color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or \
        curr_color != image[sr][sc]:
            return

        image[sr][sc] = color

        self.fill(image, sr-1, sc, color, curr_color)
        self.fill(image, sr+1, sc, color, curr_color)
        self.fill(image, sr, sc-1, color, curr_color)
        self.fill(image, sr, sc+1, color, curr_color)

    def floodFill(self, image, sr, sc, color):
        curr_color = image[sr][sc]

        if curr_color == color:
            return image

        self.fill(image, sr, sc, color, curr_color)
        return image
