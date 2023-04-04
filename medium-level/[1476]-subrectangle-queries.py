# Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in
# the constructor and supports two methods:
# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
# Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and
# bottom right coordinate is (row2,col2).
# 2. getValue(int row, int col)
#
# Returns the current value of the coordinate (row,col) from the rectangle.

# Example:
# Input
# ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
# [[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
# Output
# [null,1,null,100,100,null,20]
# Explanation
# SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
# subrectangleQueries.getValue(0, 0); // return 1
# subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
# subrectangleQueries.getValue(0, 0); // return 100
# subrectangleQueries.getValue(2, 2); // return 100
# subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
# subrectangleQueries.getValue(2, 2); // return 20

# --------------- Runtime 191 ms, beats 58.7%. Memory 15.9MB, beats 57.76% ---------------
from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
