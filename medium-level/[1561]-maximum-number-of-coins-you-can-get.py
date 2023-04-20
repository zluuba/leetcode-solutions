# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
# - In each step, you will choose any 3 piles of coins (not necessarily consecutive).
# - Of your choice, Alice will pick the pile with the maximum number of coins.
# - You will pick the next pile with the maximum number of coins.
# - Your friend Bob will pick the last pile.
# - Repeat until there are no more piles of coins.

# Given an array of integers piles where piles[i] is the number of coins in the ith pile.
# Return the maximum number of coins that you can have.

# Example:
# Input: piles = [2,4,1,2,7,8]
# Output: 9
# Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins,
# you the pile with 7 coins and Bob the last one.
# Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
# The maximum number of coins which you can have are: 7 + 2 = 9.
# On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7)
# you only get 2 + 4 = 6 coins which is not optimal.

# --------------- Runtime 591 ms, beats 97.37%. Memory 26.7MB, beats 36.84% ---------------
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        length = len(piles)
        piles = sorted(piles, reverse=True)[:length - (length // 3)]    # del Bobs coins

        my_coins = [coin for coin in piles[1::2]]
        return sum(my_coins)
