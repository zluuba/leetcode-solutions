# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# --------------- Runtime 61 ms, beats 84.66%. Memory 15.2MB, beats 41.36% ---------------


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        passed_nums = dict()

        for ind, num in enumerate(nums):
            looking_for = target - num

            if looking_for in passed_nums:
                return [passed_nums[looking_for], ind]
            else:
                passed_nums[num] = ind


# Alternative solution. Use less memory (do not create dictionary), but much slower
# --------------- Runtime 603 ms, beats 39.88%. Memory 14.9MB, beats 92.46% ---------------


class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for ind, num in enumerate(nums):
            looking_for = target - num

            if looking_for in nums[ind + 1:]:
                looking_for_ind = nums[ind + 1:].index(looking_for)
                return [ind, looking_for_ind + (ind + 1)]
