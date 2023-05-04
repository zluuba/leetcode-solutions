# https://leetcode.com/problems/dota2-senate/

# In the world of Dota2, there are two parties: the Radiant and the Dire.
# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in
# the Dota2 game. The voting for this change is a round-based procedure.
# In each round, each senator can exercise one of the two rights:
# - Ban one senator's right: A senator can make another senator lose all his rights in this and all
#   the following rounds.
# - Announce the victory: If this senator found the senators who still have rights to vote are all from the same party,
#   he can announce the victory and decide on the change in the game.

# Given a string senate representing each senator's party belonging.
# The character 'R' and 'D' represent the Radiant party and the Dire party.
# Then if there are n senators, the size of the given string will be n.
# The round-based procedure starts from the first senator to the last senator in the given order.
# This procedure will last until the end of voting. All the senators who have lost their rights will be skipped
# during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party.
# Predict which party will finally announce the victory and change the Dota2 game.
# The output should be "Radiant" or "Dire".

# Example 1:
# Input: senate = "RD"
# Output: "Radiant"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

# Example 2:
# Input: senate = "RDD"
# Output: "Dire"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And the third senator comes from Dire and he can ban the first senator's right in round 1.
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

# --------------- Runtime 127 ms, beats 18.4%. Memory 16.8MB, beats 5.50% ---------------


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = [], []

        for ind, senator in enumerate(senate):
            radiant.append(ind) if senator == 'R' else dire.append(ind)

        while radiant and dire:
            rc, dc = radiant.pop(0), dire.pop(0)
            length = len(senate)

            if rc < dc:
                radiant.append(dc + length)
            else:
                dire.append(rc + length)

        return 'Radiant' if radiant else 'Dire'


# Alternative solution - really slow, but was fun to write
# --------------- Runtime 1801 ms, beats 11.93%. Memory 16.3MB, beats 15.60% ---------------

class Solution2:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = 'R', 'D'
        senate = list(senate)
        pointer = 0

        while r in senate and d in senate:
            if pointer >= len(senate):
                pointer = 0

            curr_char = senate[pointer]

            if curr_char in (r, d):
                opposite_char = r if curr_char == d else d
                if opposite_char in senate[pointer:]:
                    next_char = senate[pointer:].index(opposite_char) + pointer
                else:
                    next_char = senate.index(opposite_char)
                    pointer -= 1
                senate.pop(next_char)

            pointer += 1

        return 'Radiant' if r in senate else 'Dire'
