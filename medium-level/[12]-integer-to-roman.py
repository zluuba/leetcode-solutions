# https://leetcode.com/problems/integer-to-roman/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, 2 is written as II in Roman numeral, just two one's added together.
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
# - I can be placed before V (5) and X (10) to make 4 and 9.
# - X can be placed before L (50) and C (100) to make 40 and 90.
# - C can be placed before D (500) and M (1000) to make 400 and 900.

# Given an integer, convert it to a roman numeral.

# Example 1:
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.

# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# --------------- Runtime 63 ms, beats 14.13%. Memory 16.4MB, beats 6.39% ---------------

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M',
        }

        result = ''
        for key in reversed(roman.keys()):
            if 0 < num // key:
                result += roman[key] * (num // key)
                num -= key * (num // key)

        return result


# Alternative solution - brute force
# --------------- Runtime 63 ms, beats 13.23%. Memory 16.5MB, beats 23.1% ---------------

class Solution2:
    roman = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
        90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M',
    }

    def build_roman(self, curr, result='', prev_key=1):
        if curr < 1:
            return ''
        if curr in self.roman:
            return result + self.roman[curr]

        for key in self.roman.keys():
            if key > curr or (key == 1000 and curr >= key):
                key = key if (key == 1000 and curr >= key) else prev_key
                curr -= key
                result += self.roman[key]
                result += self.build_roman(curr)
                return result

            prev_key = key

    def intToRoman(self, num: int) -> str:
        result = ''
        div = 1000
        while num:
            curr = num % div
            num -= curr
            div = div // 10 if div > 10 else 10
            result += self.build_roman(num if num else curr)
            num = curr if num else num

        return result
