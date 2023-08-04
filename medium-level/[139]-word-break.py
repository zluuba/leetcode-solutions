# https://leetcode.com/problems/word-break/

# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# --------------- Runtime 48 ms, beats 79.89%. Memory 16.4MB, beats 83.50% ---------------
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [1] + [0] * length

        for i in range(length):
            for j in range(i, length):
                if s[i:j + 1] in wordDict:
                    dp[j + 1] = max(dp[i], dp[j + 1])

        return bool(dp[-1])
