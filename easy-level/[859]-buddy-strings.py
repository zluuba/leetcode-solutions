# https://leetcode.com/problems/buddy-strings/

# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal,
# otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and
# swapping the characters at s[i] and s[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# Example 1:
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

# Example 2:
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

# Example 3:
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

# --------------- Runtime 57 ms, beats 21.22%. Memory 16.6MB, beats 28.16% ---------------

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        length = len(s)

        if length < 2:
            return False
        if s == goal:
            return len(set(s)) < len(goal)

        s, goal = list(s), list(goal)
        left, right = 0, length - 1

        while left < right and s[left] == goal[left]:
            left += 1

        while right >= 0 and s[right] == goal[right]:
            right -= 1

        if left < right:
            s[left], s[right] = s[right], s[left]

        return s == goal
