# You are given a list of strings of the same length words and a string target.
# Your task is to form target using the given words under the following rules:
# target should be formed from left to right.
# To form the ith character (0-indexed) of target,
# you can choose the kth character of the jth string in words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words,
# you can no longer use the xth character of any string in words where x <= k.
# In other words, all characters to the left of or at index k become unusuable for every string.
# Repeat the process until you form the string target.
# Notice that you can use multiple characters from the same string in words provided the conditions above are met.
# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

# Example:
# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

# --------------- Runtime 1349 ms, beats 84.5%. Memory 20.3MB, beats 99.22% ---------------
from collections import defaultdict
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        tlength = len(target)
        dp = [1] + [0 for _ in range(tlength)]

        for i in range(len(words[0])):
            counter = defaultdict(int)
            for word in words:
                counter[word[i]] += 1

            for j in range(tlength - 1, -1, -1):
                dp[j + 1] += dp[j] * counter.get(target[j], 0) % mod

        return dp[tlength] % mod


# Alternative solution (with dfs)
# --------------- Runtime 4312 ms, beats 5.84%. Memory 398.8MB, beats 7.78% ---------------


class Solution2:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        tlength = len(target)
        wlength = len(words[0])

        count = defaultdict(int)
        for word in words:
            for ind, char in enumerate(word):
                count[(ind, char)] += 1

        dp = {}

        def dfs(tindex, windex):
            if tindex == tlength:
                return 1
            if windex == wlength:
                return 0
            if (tindex, windex) in dp:
                return dp[(tindex, windex)]

            c = target[tindex]
            dp[(tindex, windex)] = dfs(tindex, windex + 1)
            dp[(tindex, windex)] += count[(windex, c)] * dfs(tindex + 1, windex + 1)
            return dp[(tindex, windex)] % mod

        return dfs(0, 0)
