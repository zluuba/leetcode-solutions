# You are given an array nums consisting of positive integers.
# You have to take each integer in the array, reverse its digits, and add it to the end of the array.
# You should apply this operation to the original integers in nums.
# Return the number of distinct integers in the final array.

# Example:
# Input: nums = [1,13,10,12,31]
# Output: 6
# Explanation: After including the reverse of each number, the resulting array is [1,13,10,12,31,1,31,1,21,13].
# The reversed integers that were added to the end of the array are underlined.
# Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
# The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).

# --------------- Runtime 716 ms, beats 84.42%. Memory 39.5MB, beats 76.5% ---------------
from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = set(nums)

        for num in nums:
            new_num = int(str(num)[::-1])
            if new_num not in result:
                result.add(new_num)

        return len(result)
