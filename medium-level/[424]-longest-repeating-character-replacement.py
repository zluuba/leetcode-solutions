# You are given a string s and an integer k. You can choose any character of the string and change it to any
# other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get
# after performing the above operations.

# --------------- Runtime 118 ms, beats 80.94%. Memory 13.9MB, beats 90.70% ---------------


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, result = 0, 0
        max_value, hashmap = 0, {}

        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right], 0)
            max_value = max(max_value, hashmap[s[right]])

            if (right - left + 1) - max_value > k:
                hashmap[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        return result
