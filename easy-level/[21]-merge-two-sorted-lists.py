# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

# --------------- Runtime 38 ms, beats 74.34%. Memory 13.9MB, beats 25.23% ---------------


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        min_node, max_node = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = min_node

        while min_node and max_node:
            while min_node.next and min_node.next.val < max_node.val:
                min_node = min_node.next

            min_node.next, max_node = max_node, min_node.next
            min_node = min_node.next

        return head
