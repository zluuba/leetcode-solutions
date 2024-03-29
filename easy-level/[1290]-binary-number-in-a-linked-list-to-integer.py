# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Given head which is a reference node to a singly-linked list. The value of each node in the linked
# list is either 0 or 1. The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.
#
# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2:
# Input: head = [0]
# Output: 0

# --------------- Runtime 28 ms, beats 86.89%. Memory 13.8MB, beats 93.14% ---------------


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_num = []

        while head:
            bin_num.append(str(head.val))
            head = head.next

        return int(''.join(bin_num), 2)
