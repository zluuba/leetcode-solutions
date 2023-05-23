# https://leetcode.com/problems/kth-largest-element-in-a-stream/

# Design a class to find the kth largest element in a stream. Note that it is the kth largest element
# in the sorted order, not the kth distinct element.
# Implement KthLargest class:
# - KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# - int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element
#   in the stream.

# Example 1:
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8

# --------------- Runtime 121 ms, beats 16.32%. Memory 21MB, beats 6.32% ---------------
from typing import List
from sortedcontainers import SortedList
import bisect


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        insert_ind = bisect.bisect(self.nums, val)
        self.nums.insert(insert_ind, val)
        return self.nums[-self.k]


# Alternative solution - using SortedList
# --------------- Runtime 134 ms, beats 14.59%. Memory 21MB, beats 6.32% ---------------

class KthLargest2:

    def __init__(self, k: int, nums: List[int]):
        self.nums = SortedList(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.nums.add(val)
        return self.nums[-self.k]


# Alternative solution - easiest
# --------------- Runtime 970 ms, beats 9.6%. Memory 20.8MB, beats 6.32% ---------------

class KthLargest3:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
