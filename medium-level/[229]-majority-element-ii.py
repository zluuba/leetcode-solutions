# https://leetcode.com/problems/majority-element-ii/

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]

# Example 3:
# Input: nums = [1,2]
# Output: [1,2]

# --------------- Runtime 110 ms, beats 62.72%. Memory 17.7MB, beats 84.36% ---------------
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_length = len(nums) / 3
        nums_count = dict()

        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1

        result = [num for num, count in nums_count.items() if count > majority_length]
        return result


# Alternative solution - using .count() method
# --------------- Runtime 121 ms, beats 15.87%. Memory 17.8MB, beats 49.91% ---------------

class Solution2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_length = len(nums) / 3
        result = []

        for num in set(nums):
            if nums.count(num) > majority_length:
                result.append(num)

        return result
