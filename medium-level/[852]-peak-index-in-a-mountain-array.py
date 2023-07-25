# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# An array arr a mountain if the following properties hold:
# - arr.length >= 3
# - There exists some i with 0 < i < arr.length - 1 such that:
#    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

# Example 1:
# Input: arr = [0,1,0]
# Output: 1

# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1

# --------------- Runtime 625 ms, beats 14.6%. Memory 30.3MB, beats 10.3% ---------------
from typing import List


# O(n)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)

        for i in range(1, length):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return i
        return -1


# --------------- Runtime 611 ms, beats 26.90%. Memory 30.2MB, beats 32.70% ---------------

# O(log(arr.length)) - binary search
class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        left, right = 1, length - 2

        while left <= right:
            middle = left + (right - left) // 2

            if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
                return middle
            elif arr[middle] > arr[middle - 1]:
                left = middle + 1
            else:
                right = middle - 1

        return -1
