# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
# In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

# Return the number of '*' in s, excluding the '*' between each pair of '|'.
# Note that each '|' will belong to exactly one pair.

# Example:
# Input: s = "l|*e*et|c**o|*de|"
# Output: 2
# Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
# The characters between the first and second '|' are excluded from the answer.
# Also, the characters between the third and fourth '|' are excluded from the answer.
# There are 2 asterisks considered. Therefore, we return 2.

# --------------- Runtime 34 ms, beats 58.86%. Memory 13.9MB, beats 45.17% ---------------


class Solution:
    def countAsterisks(self, s: str) -> int:
        asterisks = [elem.count('*') for elem in s.split('|')[::2]]
        return sum(asterisks)


# Alternative solution
# --------------- Runtime 31 ms, beats 78.26%. Memory 13.8MB, beats 92.41% ---------------


class Solution2:
    def countAsterisks(self, s: str) -> int:
        lst = s.split('|')
        even_pairs = ''

        for i in range(len(lst)):
            if i % 2 == 0:
                even_pairs += lst[i]

        return even_pairs.count('*')
