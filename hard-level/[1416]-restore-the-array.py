# https://leetcode.com/problems/restore-the-array/description/

# A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed
# as a string of digits s and all we know is that all integers in the array were in the range [1, k]
# and there are no leading zeros in the array.

# Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the
# mentioned program. Since the answer may be very large, return it modulo 109 + 7.

# Example 1:
# Input: s = "1000", k = 10000
# Output: 1
# Explanation: The only possible array is [1000]

# Example 2:
# Input: s = "1000", k = 10
# Output: 0
# Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.

# Example 3:
# Input: s = "1317", k = 2000
# Output: 8
# Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]

# --------------- Runtime 1401 ms, beats 84.42%. Memory 18.2MB, beats 83.12% ---------------


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        modulo = 10 ** 9 + 7
        length_s = len(s)
        length_t = len(str(k))

        dp = [1] + [0] * length_s

        for i in range(length_s):
            count = 0

            for j in range(i, max(-1, i - length_t), -1):
                curr = s[j:i + 1]
                if curr[0] != "0" and int(curr) <= k:
                    count += dp[j]

            if count == 0:
                return 0

            dp[i + 1] = count % modulo

        return dp[-1]


# Alternative solution
# --------------- Runtime 4759 ms, beats 5.19%. Memory 485.4MB, beats 5.19% ---------------

class Solution2:
    def numberOfArrays(self, s: str, k: int) -> int:
        modulo = 10 ** 9 + 7
        length_s = len(s)
        length_t = len(str(k))

        count = [0] * (length_s + 1)
        count[0], count[1] = 1, 1

        for i in range(1, length_s):
            for j in range(length_t):
                if i - j >= 0:
                    if 1 <= int(s[i - j:i + 1]) <= k and s[i - j:i + 1][0] != "0":
                        count[i + 1] += count[i - j]

        return count[-1] % modulo
