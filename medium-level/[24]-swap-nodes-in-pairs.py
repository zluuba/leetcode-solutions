# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
# the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# --------------- Runtime 49 ms, beats 14.37%. Memory 16.3MB, beats 23.7% ---------------
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node, node.next = node.next, node.next.next
            node = node.next

        return head


# Alternative solution
# --------------- Runtime 46 ms, beats 19.83%. Memory 16.2MB, beats 23.7% ---------------

class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0, head)
        prev, curr = node, head

        while curr and curr.next:
            first = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = first
            prev.next = second

            prev, curr = curr, first

        return node.next
