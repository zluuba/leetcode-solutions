# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        length = len(nums)
        counter = 0
        for i in range(0, length - 1):
            for j in range(i, length):
                if nums[i] == nums[j] and i < j:
                    counter += 1
        return counter
