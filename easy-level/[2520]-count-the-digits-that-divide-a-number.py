# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.

# Example 1:
# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.

# Example 2:
# Input: num = 121
# Output: 2
# Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

# Example 3:
# Input: num = 1248
# Output: 4
# Explanation: 1248 is divisible by all of its digits, hence the answer is 4.

# --------------- Runtime 20 ms, beats 99.3%. Memory 13.9MB, beats 40.81% ---------------


class Solution:
    def countDigits(self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        result = 0
        for i in nums:
            if num % i == 0:
                result += 1

        return result


# Alternative solution - list comprehensions
# --------------- Runtime 40 ms, beats 22.31%. Memory 13.8MB, beats 40.81% ---------------


class Solution2:
    def countDigits(self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        result = [1 for n in nums if num % n == 0]
        return sum(result)


# Alternative solution - loop
# --------------- Runtime 40 ms, beats 22.31%. Memory 13.8MB, beats 40.81% ---------------


class Solution3:
    def countDigits(self, num: int) -> int:
        result = 0
        for i in str(num):
            if num % int(i) == 0:
                result += 1

        return result
