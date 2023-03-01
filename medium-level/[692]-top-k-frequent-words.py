# Given an array of strings words and an integer k, return the k most frequent strings.
#
# Return the answer sorted by the frequency from highest to lowest. Sort the words
# with the same frequency by their lexicographical order.

# Example:
# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.

# --------------- Runtime 62 ms, beats 47.52%. Memory 13.9MB, beats 57.35% ---------------


from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}

        for word in set(words):
            frequency[word] = words.count(word) + frequency.get(word, 0)

        sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
        result = [sorted_frequency[i][0] for i in range(k)]
        return result
