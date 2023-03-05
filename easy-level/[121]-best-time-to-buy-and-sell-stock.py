# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# --------------- Runtime 1092 ms, beats 60.47%. Memory 25MB, beats 83.14% ---------------
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0

        for sell in prices:
            if sell < buy:
                buy = sell

            profit = max(sell - buy, profit)

        return profit
