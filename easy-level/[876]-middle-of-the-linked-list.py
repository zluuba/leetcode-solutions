# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

# --------------- Runtime 42 ms, beats 23.52%. Memory 13.8MB, beats 48.13% ---------------


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        while head != None:
            array.append(head)
            head = head.next
        middle = len(array) // 2
        return array[middle]
