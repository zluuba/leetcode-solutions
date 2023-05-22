# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# --------------- Runtime 102 ms, beats 85.96%. Memory 21MB, beats 41.2% ---------------
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [pair[0] for pair in Counter(nums).most_common(k)]


# Alternative solution - detailed
# --------------- Runtime 1796 ms, beats 5.1%. Memory 21.1MB, beats 30.27% ---------------

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        counts = [(num, nums.count(num)) for num in set(nums)]
        counts.sort(key=lambda pair: pair[1], reverse=True)

        return [num for num, count in counts[:k]]
