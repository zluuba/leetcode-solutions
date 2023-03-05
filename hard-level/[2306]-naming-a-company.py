# You are given an array of strings ideas that represents a list of names to be used in the process of
# naming a company. The process of naming a company is as follows:
#
# Choose 2 distinct names from ideas, call them ideaA and ideaB.
# Swap the first letters of ideaA and ideaB with each other.
# If both of the new names are not found in the original ideas, then the name ideaA ideaB
# (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
# Otherwise, it is not a valid name.
# Return the number of distinct valid names for the company.

# --------------- Runtime 879 ms, beats 65.22%. Memory 28.4MB, beats 64.13% ---------------
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = {}
        for idea in ideas:
            first_char = idea[0]
            word = idea[1:]
            if first_char in groups:
                groups[first_char].add(word)
            else:
                groups[first_char] = {word}

        result = 0
        for key1 in groups:
            for key2 in groups:
                if key1 != key2:
                    dupl = sum([1 for x in groups[key1] if x in groups[key2]])
                    result += (len(groups[key1]) - dupl) * (len(groups[key2]) - dupl)

        return result
