# Given the head of a singly linked list, reverse the list, and return the reversed list.

# --------------- Runtime 42 ms, beats 42.99%. Memory 20.4MB, beats 13.89% ---------------


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head

        head.next = None
        return new_head
