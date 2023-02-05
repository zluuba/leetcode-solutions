# Given two strings s and p, return an array of all the start indices of p's anagrams in s.
# You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# --------------- Runtime 3976 ms, beats 13.65%. Memory 15.2MB, beats 27% ---------------


class Solution:
    def get_dict(self, string):
        d = dict()
        for char in set(string):
            count = string.count(char)
            d[char] = count
        return d

    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        dict_p = self.get_dict(p)

        for ind, char in enumerate(s):
            if len(s) - ind < len(p):
                break
            chunk = s[ind:len(p) + ind]
            dict_chunk = self.get_dict(chunk)

            if dict_chunk == dict_p:
                res.append(ind)
        return res
