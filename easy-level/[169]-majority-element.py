# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# --------------- Runtime 173 ms, beats 33.21%. Memory 18MB, beats 5.24% ---------------
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums), key=nums.count)


# Alternative solution - sorting
# --------------- Runtime 184 ms, beats 10.23%. Memory 17.9MB, beats 5.24% ---------------

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums), key=lambda num: nums.count(num), reverse=True)
        return sorted_nums[0]


# Alternative solution - using hashmap
# --------------- Runtime 167 ms, beats 58.4%. Memory 17.9MB, beats 5.24% ---------------

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in set(nums):
            hashmap[num] = nums.count(num)

        max_val = max(hashmap.items(), key=lambda item: item[1])
        return max_val[0]


# Alternative solution - two vars
# --------------- Runtime 169 ms, beats 49.13%. Memory 18MB, beats 5.24% ---------------

class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        major_num, counter = 0, 0

        for num in set(nums):
            curr_count = nums.count(num)
            if curr_count > counter:
                major_num = num
                counter = curr_count

        return major_num
