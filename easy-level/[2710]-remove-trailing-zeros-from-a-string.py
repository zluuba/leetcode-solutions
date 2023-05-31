# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

# Example 1:
# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

# Example 2:
# Input: num = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".

# --------------- Runtime 43 ms, beats 98.13%. Memory 16.4MB, beats 89.46% ---------------

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')


# Alternative solution - without .strip() method
# --------------- Runtime 66 ms, beats 34.75%. Memory 16.4MB, beats 89.46% ---------------

class Solution2:
    def removeTrailingZeros(self, num: str) -> str:
        while num[-1] == '0':
            num = num[:-1]

        return num


# Alternative solution - using right pointer
# --------------- Runtime 66 ms, beats 34.75%. Memory 16.4MB, beats 89.46% ---------------

class Solution3:
    def removeTrailingZeros(self, num: str) -> str:
        right = len(num) - 1
        while num[right] == '0':
            right -= 1

        return num[:right + 1]
