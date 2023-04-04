# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# --------------- Runtime 97 ms, beats 49.27%. Memory 14.1MB, beats 93.82% ---------------
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0

        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1

        p1, p2 = 0, len1
        middle = (len1 + len2 + 1) // 2

        while p1 <= p2:
            i = (p1 + p2) // 2
            j = middle - i
            if i < len1 and nums2[j - 1] > nums1[i]:
                p1 = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                p2 = i - 1
            else:
                if i == 0: left = nums2[j - 1]
                elif j == 0: left = nums1[i - 1]
                else: left = max(nums1[i - 1], nums2[j - 1])

                if (len1 + len2) % 2 == 1:
                    return left

                if i == len1: right = nums2[j]
                elif j == len2: right = nums1[i]
                else: right = min(nums1[i], nums2[j])

                return (left + right) / 2


# Alternative solution with complexity O(NlogN), N=m+n
# --------------- Runtime 83 ms, beats 96.45%. Memory 14.2MB, beats 55.8% ---------------

class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if not nums:
            return 0

        length = len(nums)
        middle = length // 2
        if length % 2 == 0:
            return (nums[middle - 1] + nums[middle]) / 2
        return nums[middle]
