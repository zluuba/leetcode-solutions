# There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.
# In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.
# Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom,
# and a positive integer k, return the maximum total value of coins you can have in your wallet if
# you choose exactly k coins optimally.

# Example 1:
# Input: piles = [[1,100,3],[7,8,9]], k = 2
# Output: 101
# Explanation:
# The above diagram shows the different ways we can choose k coins.
# The maximum total we can obtain is 101.

# Example 2:
# Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
# Output: 706
# Explanation:
# The maximum total can be obtained if we choose all coins from the last pile.

# --------------- Runtime 5155 ms, beats 36.48%. Memory 38.5MB, beats 77.36% ---------------
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        length = len(piles)
        dp = [[-1] * (k + 1) for _ in range(length)]

        def search(pile, coins):
            if pile == length:
                return 0
            if dp[pile][coins] != -1:
                return dp[pile][coins]

            dp[pile][coins] = search(pile + 1, coins)
            curr_pile = 0

            for i in range(min(len(piles[pile]), coins)):
                curr_pile += piles[pile][i]
                dp[pile][coins] = max(
                    dp[pile][coins], curr_pile + search(pile + 1, coins - i - 1)
                )

            return dp[pile][coins]

        return search(0, k)
