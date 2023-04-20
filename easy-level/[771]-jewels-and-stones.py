# https://leetcode.com/problems/jewels-and-stones/

# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

# --------------- Runtime 27 ms, beats 92.32%. Memory 13.8MB, beats 51.65% ---------------


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        for stone in stones:
            if stone in jewels:
                result += 1

        return result


# Alternative solution with list comprehension
# --------------- Runtime 28 ms, beats 89.47%. Memory 13.9MB, beats 51.65% ---------------


class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = [1 for stone in stones if stone in jewels]
        return sum(result)
