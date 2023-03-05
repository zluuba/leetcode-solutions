# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
#
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
#
# Return the maximum number of words that appear in a single sentence.

# --------------- Runtime 42 ms, beats 74.5%. Memory 13.9MB, beats 36.18% ---------------
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        for sentence in sentences:
            length = len(sentence.split())
            maximum = max(maximum, length)

        return maximum
