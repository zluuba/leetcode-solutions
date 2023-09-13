# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Given the head of a linked list head, in which each node contains an integer value.
# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
# Return the linked list after insertion.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Example 1:
# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after
# inserting the new nodes (nodes in blue are the inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
# There are no more adjacent nodes, so we return the linked list.

# Example 2:
# Input: head = [7]
# Output: [7]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after
# inserting the new nodes.
# There are no pairs of adjacent nodes, so we return the initial linked list.

# --------------- Runtime 100 ms, beats 58.52%. Memory 21.2MB, beats 12.59% ---------------
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_gcd(num1, num2):
            if num1 < num2:
                num1, num2 = num2, num1
            while num2 != 0:
                num1, num2 = num2, num1 % num2
            return num1

        tree = node = head

        while node.next:
            gcd = get_gcd(node.val, node.next.val)
            node.next = ListNode(gcd, node.next)
            node = node.next.next

        return tree
