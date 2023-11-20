# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

# You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage
# at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal,
# paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.
# You are also given a 0-indexed integer array travel where travel[i] is the number of
# minutes needed to go from house i to house i + 1.
# There are three garbage trucks in the city, each responsible for picking up one type of garbage.
# Each garbage truck starts at house 0 and must visit each house in order;
# however, they do not need to visit every house.
# Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage,
# the other two trucks cannot do anything.

# Return the minimum number of minutes needed to pick up all the garbage.

# Example:
# Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
# Output: 21
# Explanation:
# The paper garbage truck:
# 1. Travels from house 0 to house 1
# 2. Collects the paper garbage at house 1
# 3. Travels from house 1 to house 2
# 4. Collects the paper garbage at house 2
# Altogether, it takes 8 minutes to pick up all the paper garbage.
# The glass garbage truck:
# 1. Collects the glass garbage at house 0
# 2. Travels from house 0 to house 1
# 3. Travels from house 1 to house 2
# 4. Collects the glass garbage at house 2
# 5. Travels from house 2 to house 3
# 6. Collects the glass garbage at house 3
# Altogether, it takes 13 minutes to pick up all the glass garbage.
# Since there is no metal garbage, we do not need to consider the metal garbage truck.
# Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.

# --------------- Runtime 729 ms, beats 100%. Memory 39.3MB, beats 61.98% ---------------
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        houses = len(travel)
        time_in_way = 0

        for garb_type in ['M', 'P', 'G']:
            house_ind = houses

            while (house_ind > 0) and (garb_type not in garbage[house_ind]):
                house_ind -= 1

            time_in_way += sum(travel[:house_ind])

        garbage_picking_time = sum([len(garb) for garb in garbage])
        return garbage_picking_time + time_in_way


# Alternative solution - classic
# --------------- Runtime 799 ms, beats 91.24%. Memory 39.3MB, beats 61.98% ---------------

class Solution2:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        garbage_picking_time = 0
        m_truck, p_truck, g_truck = 0, 0, 0

        for house, garb in enumerate(garbage):
            if 'M' in garb:
                m_truck = house
            if 'P' in garb:
                p_truck = house
            if 'G' in garb:
                g_truck = house

            garbage_picking_time += len(garb)

        time_in_way = sum(travel[:m_truck]) + sum(travel[:p_truck]) + sum(travel[:g_truck])
        return garbage_picking_time + time_in_way
