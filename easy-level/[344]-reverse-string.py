# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# --------------- Runtime 190 ms, beats 91.7%. Memory 18.4MB, beats 36.2% ---------------
from typing import List


# Do not return anything, modify s in-place instead.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


# Alternative solution
# --------------- Runtime 194 ms, beats 80.67%. Memory 18.7MB, beats 6.80% ---------------
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


# Alternative solution
# --------------- Runtime 387 ms, beats 5.27%. Memory 18.4MB, beats 77.79% ---------------

class Solution3:
    def reverseString(self, s: List[str]) -> None:
        [s.append(s.pop(i)) for i in range(-2, -(len(s) + 1), -1)]
