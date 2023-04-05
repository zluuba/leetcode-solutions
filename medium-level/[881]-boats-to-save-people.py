# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where
# each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time,
# provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.

# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

# Example 2:
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)

# --------------- Runtime 443 ms, beats 96.44%. Memory 20.9MB, beats 58.28% ---------------
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people = sorted(people, reverse=True)

        p1, p2 = 0, len(people) - 1
        while p1 <= p2:
            boat = people[p1]
            p1 += 1
            if boat + people[p2] <= limit:
                boat += people[p2]
                p2 -= 1

            boats += 1

        return boats
