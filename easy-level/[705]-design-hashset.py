# https://leetcode.com/problems/design-hashset/

# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:
# - void add(key) Inserts the value key into the HashSet.
# - bool contains(key) Returns whether the value key exists in the HashSet or not.
# - void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

# Example:
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)

# --------------- Runtime 319 ms, beats 31.94%. Memory 24MB, beats 17.23% ---------------


class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.hash_set = [ListNode(0) for _ in range(10 ** 4)]

    def add(self, key: int) -> None:
        node = self.get_node(key)
        while node.next:
            if node.next.key == key:
                return
            node = node.next

        node.next = ListNode(key)

    def remove(self, key: int) -> None:
        node = self.get_node(key)
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def contains(self, key: int) -> bool:
        node = self.get_node(key)
        while node.next:
            if node.next.key == key:
                return True
            node = node.next
        return False

    def get_node(self, key):
        index = key % len(self.hash_set)
        return self.hash_set[index]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
