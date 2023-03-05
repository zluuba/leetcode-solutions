# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money
# the i^th customer has in the j^th bank. Return the wealth that the richest customer has.
#
# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.

# --------------- Runtime 49 ms, beats 95.40%. Memory 13.9MB, beats 24.18% ---------------
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = [sum(acc) for acc in accounts]
        return max(sums)
