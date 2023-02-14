# Given an integer num, return the number of digits in num that divide num.
#
# An integer val divides nums if nums % val == 0.

# Fastest solution
# --------------- Runtime 20 ms, beats 99.3%. Memory 13.9MB, beats 40.81% ---------------


class Solution:
    def countDigits(self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        result = 0
        for i in nums:
            if num % i == 0:
                result += 1

        return result


# Alternative solution. Use only list comprehensions
# --------------- Runtime 40 ms, beats 22.31%. Memory 13.8MB, beats 40.81% ---------------


class Solution2:
    def countDigits(self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        result = [1 for n in nums if num % n == 0]
        return sum(result)


# Alternative solution. One for loop.
# --------------- Runtime 40 ms, beats 22.31%. Memory 13.8MB, beats 40.81% ---------------


class Solution3:
    def countDigits(self, num: int) -> int:
        result = 0
        for i in str(num):
            if num % int(i) == 0:
                result += 1

        return result
