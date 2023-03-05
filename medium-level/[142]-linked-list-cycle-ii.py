# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again
# by continuously following the next pointer. Internally, pos is used to denote the index of the node
# that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
# Note that pos is not passed as a parameter.
#
# Do not modify the linked list.

# --------------- Runtime 49 ms, beats 84.60%. Memory 17.3MB, beats 91.59% ---------------
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p2 and p2.next:
            p1, p2 = p1.next, p2.next.next
            if p1 == p2:
                tmp = p1

                while head != tmp:
                    head = head.next
                    tmp = tmp.next
                return head
