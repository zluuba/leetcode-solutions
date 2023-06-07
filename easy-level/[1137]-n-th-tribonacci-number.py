# https://leetcode.com/problems/n-th-tribonacci-number/

# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537

# --------------- Runtime 38 ms, beats 69.19%. Memory 16.3MB, beats 15.88% ---------------

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1

        t0, t1, t2 = 0, 1, 1
        num = 2

        while num < n:
            curr = t0 + t1 + t2
            t0, t1, t2 = t1, t2, curr
            num += 1

        return t2


# Alternative solution - exotic
# --------------- Runtime 45 ms, beats 44.41%. Memory 16.2MB, beats 49.35% ---------------

class Solution2:
    def tribonacci(self, n: int) -> int:
        cache = [0, 1, 1]
        curr = 2

        while curr < n:
            tmp = sum(cache[-3:])
            cache.append(tmp)
            curr += 1

        return cache[-1] if n > 1 else cache[n]
