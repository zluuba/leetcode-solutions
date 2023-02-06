# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
# For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
#
# Given a string n that represents a positive decimal integer, return the minimum number
# of positive deci-binary numbers needed so that they sum up to n.

# Fastest/shortest solution.
# Any length of number can be expressed through (maximum) 9 combinations of deci-binary numbers,
# so we just find the maximum digit in the number.
# --------------- Runtime 44 ms, beats 97.92%. Memory 14.8MB, beats 48.40% ---------------


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(set(n)))


# Alternative solution. Shows the solution algorithm.
# --------------- Runtime 8049 ms, beats 5.5%. Memory 17.2MB, beats 9.13% ---------------


class Solution2:
    def minPartitions(self, n: str) -> int:
        number = int(n)
        counter = 0

        while number > 0:
            binary = ['0' if int(num) == 0 else '1' for num in n]

            binary_int = int(''.join(binary))
            number -= binary_int
            n = str(number)
            counter += 1

        return counter
