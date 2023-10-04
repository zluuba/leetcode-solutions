# https://leetcode.com/problems/design-hashmap/

# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
#  - MyHashMap() initializes the object with an empty map.
#  - void put(int key, int value) inserts a (key, value) pair into the HashMap.
#    If the key already exists in the map, update the corresponding value.
#  - int get(int key) returns the value to which the specified key is mapped,
#    or -1 if this map contains no mapping for the key.
#  - void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

# Example:
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

# --------------- Runtime 181 ms, beats 83.49%. Memory 19.68MB, beats 66.49% ---------------

class MyHashMap:
    def __init__(self):
        self.size = 2023
        self.hashmap = [[]] * self.size

    def put(self, key: int, value: int) -> None:
        hash = key // self.size
        array = self.hashmap[hash]

        if not array:
            array = [-1] * self.size
            self.hashmap[hash] = array

        index = key - (hash * self.size)
        array[index] = value

    def get(self, key: int) -> int:
        hash = key // self.size
        array = self.hashmap[hash]

        if not array:
            return -1

        index = key - (hash * self.size)
        return array[index]

    def remove(self, key: int) -> None:
        hash = key // self.size
        array = self.hashmap[hash]

        if not array:
            return

        index = key - (hash * self.size)
        array[index] = -1


# Alternative solution - 1 min. hardcode
# --------------- Runtime 321 ms, beats 22.68%. Memory 42.2MB, beats 7.51% ---------------

class MyHashMap2:
    def __init__(self):
        self.hashmap = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key]

    def remove(self, key: int) -> None:
        self.hashmap[key] = -1
