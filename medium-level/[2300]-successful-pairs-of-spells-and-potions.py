# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

# You are given two positive integer arrays spells and potions, of length n and m respectively,
# where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
# You are also given an integer success. A spell and potion pair is considered successful
# if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form
# a successful pair with the ith spell.

# Example:
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.

# --------------- Runtime 1123 ms, beats 99.88%. Memory 37.5MB, beats 22.31% ---------------
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        successful_spells = {i: 0 for i in sorted(set(spells))}
        potions = sorted(potions, reverse=True)
        potion_ind = 0

        for spell in successful_spells:
            while potion_ind < len(potions) and \
                    potions[potion_ind] * spell >= success:
                potion_ind += 1

            successful_spells[spell] = potion_ind

        return [successful_spells[spell] for spell in spells]
