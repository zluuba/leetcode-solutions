# You are given a positive integer array nums.
#
# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.
#
# Note that the absolute difference between two integers x and y is defined as |x - y|.

# --------------- Runtime 159 ms, beats 30.33%. Memory 14MB, beats 90.90% ---------------


class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        elem_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            digs = str(num)
            for char in digs:
                digit_sum += int(char)

        return abs(elem_sum - digit_sum)


# Alternative solution. Shorter, use map()
# --------------- Runtime 129 ms, beats 85.18%. Memory 14.2MB, beats 53.11% ---------------


class Solution2:
    def differenceOfSum(self, nums: list[int]) -> int:
        digits = ''.join([str(n) for n in nums])
        digit_sum = sum(list(map(int, digits)))
        return abs(sum(nums) - digit_sum)
