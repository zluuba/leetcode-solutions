# https://leetcode.com/problems/partition-labels/

# You are given a string s. We want to partition the string into as many parts as possible so that each letter
# appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:
# Input: s = "eccbbbbdec"
# Output: [10]

# --------------- Runtime 46 ms, beats 53.51%. Memory 16.1MB, beats 88.53% ---------------
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        chunk_size, max_index = 0, 0
        chars = {char: index for index, char in enumerate(s)}

        for index, char in enumerate(s):
            max_index = max(max_index, chars[char])
            chunk_size += 1

            if index == max_index:
                result.append(chunk_size)
                chunk_size = 0

        return result


# Alternative solution - sliding window
# --------------- Runtime 129 ms, beats 5.25%. Memory 16.2MB, beats 61.76% ---------------

class Solution2:
    def partitionLabels(self, s: str) -> List[int]:
        length = len(s)
        result = []
        left, right = 0, 1

        while left < length:
            curr_chunk = s[left:right]
            next_chunk = s[right:]

            common_letters = set(curr_chunk) & set(next_chunk)

            if (right >= length) or (not common_letters):
                result.append(right - left)
                left = right

            right += 1

        return result
