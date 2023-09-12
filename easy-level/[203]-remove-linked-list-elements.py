# https://leetcode.com/problems/remove-linked-list-elements/

# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# --------------- Runtime 60 ms, beats 87.38%. Memory 19.9MB, beats 53.35% ---------------
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_tree = ListNode()
        new_tree.next = head
        node = new_tree

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return new_tree.next
