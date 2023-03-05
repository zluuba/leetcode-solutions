# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographically in this alien language.

# --------------- Runtime 36 ms, beats 75.82%. Memory 13.8MB, beats 76.45% ---------------
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            for j in range(len(word1)):
                if j == len(word2):
                    return False

                if word1[j] != word2[j]:
                    if order.index(word1[j]) > order.index(word2[j]):
                        return False
                    break

        return True
