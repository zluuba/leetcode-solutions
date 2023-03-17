# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# Example:
# Input: num = 9669
# Output: 9969
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.

# --------------- Runtime 27 ms, beats 87.88%. Memory 13.9MB, beats 42.80% ---------------


class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))


# Alternative solution. Long, without replace method
# --------------- Runtime 27 ms, beats 87.88%. Memory 13.8MB, beats 93.51% ---------------


class Solution2:
    def maximum69Number(self, num: int) -> int:
        num = str(num)

        if len(set(num)) == 1:
            if set(num) == set('9'):
                return int(num)
            return int('9' + num[1:])

        first_six = num.find('6')
        res_num = num[:first_six] + '9' + num[first_six + 1:]
        return int(res_num)
