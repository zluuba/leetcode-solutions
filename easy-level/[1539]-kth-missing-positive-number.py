# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
#
# Return the kth positive integer that is missing from this array.
#
# Example:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# --------------- Runtime 173 ms, beats 16.30%. Memory 14MB, beats 44.89% ---------------
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing, missing_count = 0, 0
        for i in range(1, len(arr) + k + 1):
            if i not in arr:
                missing = i
                missing_count += 1
                if missing_count == k:
                    return missing


# --------------- Runtime 154 ms, beats 19.71%. Memory 14MB, beats 80.43% ---------------


class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        volume = arr[-1]
        full_arr = list(range(1, volume + 1))
        missing = [x for x in full_arr if x not in arr]

        if len(missing) < k:
            k = k - len(missing)
            last_num = missing[-1] if missing else 0
            return max(last_num, volume) + k

        return missing[k - 1]
