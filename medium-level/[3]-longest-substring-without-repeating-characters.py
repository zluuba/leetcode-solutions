# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# --------------- Runtime 237 ms, beats 19.9%. Memory 14MB, beats 87.96% ---------------


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_subs = 0

        p1, p2 = 0, 1
        while p2 <= len(s):
            curr_subs = s[p1:p2]
            if len(curr_subs) != len(set(curr_subs)) or p2 == len(s):
                longest_subs = max(longest_subs, len(set(curr_subs)))
                p1 += 1
            p2 += 1

        return longest_subs
