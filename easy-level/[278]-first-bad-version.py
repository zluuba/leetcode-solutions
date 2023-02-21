# You are a product manager and currently leading a team to develop a new product. Unfortunately,
# the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# --------------- Runtime 31 ms, beats 67.89%. Memory 13.8MB, beats 51.48% ---------------


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        p1, p2 = 1, n

        while p1 <= p2:
            middle = (p1 + p2) // 2

            if isBadVersion(middle):
                p2 = middle - 1
            else:
                p1 = middle + 1

        return p1
