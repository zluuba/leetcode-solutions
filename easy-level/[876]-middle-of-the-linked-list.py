# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

# --------------- Runtime 35 ms, beats 49.62%. Memory 13.8MB, beats 93.85% ---------------
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        while head is not None:
            array.append(head)
            head = head.next

        middle = len(array) // 2
        return array[middle]
