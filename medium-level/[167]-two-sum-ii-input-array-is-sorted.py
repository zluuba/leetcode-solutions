# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1]
# and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2,
# added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# --------------- Runtime 121 ms, beats 93.77%. Memory 14.9MB, beats 80.45% ---------------
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1

        while p1 < p2:
            diff = numbers[p1] + numbers[p2]
            if diff == target:
                break
            elif diff > target:
                p2 -= 1
            else:
                p1 += 1

        return [p1 + 1, p2 + 1]
