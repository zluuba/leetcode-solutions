# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

# --------------- Runtime 38 ms, beats 90.28%. Memory 16.3MB, beats 86.5% ---------------
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def get_comb(nums, acc):
            if not nums:
                return acc

            num, other = nums[0], nums[1:]

            for char in phone_letters[num]:
                combinations.append(get_comb(other, acc + char))

        combinations = []
        get_comb(digits, '')

        return list(filter(lambda comb: comb, combinations))
